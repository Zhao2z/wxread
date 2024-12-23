import os
import json
import time
import random
import logging
import hashlib
import requests
import urllib.parse
from push import push
from capture import headers as local_headers, cookies as local_cookies, data

# 配置日志格式
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)-8s - %(message)s',handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# github action部署用
# 从环境变量获取 headers、cookies等值(如果不存在使用默认本地值)
# 每一次代表30秒，比如你想刷1个小时这里填120，你只需要签到这里填2次
env_num = os.getenv('READ_NUM')
env_method = os.getenv('PUSH_METHOD')
env_headers = os.getenv('WXREAD_HEADERS')
env_cookies = os.getenv('WXREAD_COOKIES')

number = int(env_num) if env_num not in (None, '') else 120
headers = json.loads(json.dumps(eval(env_headers))) if env_headers else local_headers
cookies = json.loads(json.dumps(eval(env_cookies))) if env_cookies else local_cookies

# 加密盐及其它默认值
KEY = "3c5c8717f3daf09iop3423zafeqoi"
COOKIE_DATA = {"rq": "%2Fweb%2Fbook%2Fread"}
READ_URL = "https://weread.qq.com/web/book/read"
RENEW_URL = "https://weread.qq.com/web/login/renewal"


def encode_data(data):
    return '&'.join(f"{k}={urllib.parse.quote(str(data[k]), safe='')}" for k in sorted(data.keys()))


def cal_hash(input_string):
    _7032f5 = 0x15051505
    _cc1055 = _7032f5
    length = len(input_string)
    _19094e = length - 1

    while _19094e > 0:
        _7032f5 = 0x7fffffff & (_7032f5 ^ ord(input_string[_19094e]) << (length - _19094e) % 30)
        _cc1055 = 0x7fffffff & (_cc1055 ^ ord(input_string[_19094e - 1]) << _19094e % 30)
        _19094e -= 2

    return hex(_7032f5 + _cc1055)[2:].lower()


def get_wr_skey():
    response = requests.post(RENEW_URL, headers=headers, cookies=cookies,
                             data=json.dumps(COOKIE_DATA, separators=(',', ':')))
    for cookie in response.headers.get('Set-Cookie', '').split(';'):
        if "wr_skey" in cookie:
            return cookie.split('=')[-1][:8]
    return None


index = 1
while index <= number:
    data['ct'] = int(time.time())
    data['ts'] = int(time.time() * 1000)
    data['rn'] = random.randint(0, 1000)
    data['sg'] = hashlib.sha256(f"{data['ts']}{data['rn']}{KEY}".encode()).hexdigest()
    data['s'] = cal_hash(encode_data(data))

    logging.info(f"⏱️ 尝试第 {index} 次阅读...")
    response = requests.post(READ_URL, headers=headers, cookies=cookies, data=json.dumps(data, separators=(',', ':')))
    resData = response.json()

    if 'succ' in resData:
        index += 1
        time.sleep(30)
        logging.info(f"✅ 阅读成功，阅读进度：{(index-1) * 0.5} 分钟")

    else:
        logging.warning("❌ cookie 已过期，尝试刷新...")
        new_skey = get_wr_skey()
        if new_skey:
            cookies['wr_skey'] = new_skey
            logging.info(f"✅ 密钥刷新成功，新密钥：{new_skey}")
            logging.info(f"🔄 重新本次阅读。")
        else:
            logging.error("❌ 无法获取新密钥，终止运行。")
            push("❌ 无法获取新密钥，终止运行。", env_method)
            raise Exception("❌ 无法获取新密钥，终止运行。")
    data.pop('s')

logging.info("🎉 阅读脚本已完成！")

if env_method not in (None, ''):
    completed = index - 1  # 实际完成的次数
    total_time = completed * 0.5  # 阅读时长（分钟）
    completion_rate = (completed / number) * 100  # 完成率

    message = (
        "微信读书自动阅读完成！\n"
        f"📚 目标次数：{number}次\n"
        f"✅ 成功次数：{completed}次\n"
        f"💯 完成率：{completion_rate:.1f}%\n"
        f"⏱️ 阅读时长：{total_time}分钟"
    )

    logging.info(f"⏱️ 开始推送... {message}")
    push(message, env_method)
