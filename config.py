# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import random
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM') or 120)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# read接口的bash命令，本地部署时可对应替换headers、cookies
# curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    'ptcz': '1cd2978655d7c327695ef59c013b4efa29dec9a37ce0a2bf336874962a7cc858',
    'pgv_pvid': '9291276337',
    'o_cookie': '1758454412',
    '_qimei_q36': '',
    'LW_uid': 'l1N7v1y6A2E662f54733g3a2b6',
    'LW_sid': 'w1I7w1g6I2x6R4o063I7k1Z1J3',
    '_clck': '1rg6idj|1|fn6|0',
    'wr_localvid': 'aed32df0816e8002eaedf12',
    'wr_name': '%E6%96%BC%E6%98%AF%E6%8A%8A%E8%A9%A9%E6%91%BA%E7%96%8A',
    'wr_avatar': 'https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0003-TmA2mZmwnna9IzVRHumimd8%2F0',
    'eas_sid': 'r1Y772a2r8n2q7W035w0l2r6V9',
    'qq_domain_video_guid_verify': 'f257275ca9c88543',
    'RK': '61fYOI4TFs',
    'pac_uid': '0_CC0jFYmRNXbAf',
    '_qimei_h38': '98e58604d3919694bd80bd760300000df1830d',
    'wr_gender': '1',
    'wr_pf': 'NaN',
    'suid': 'user_0_CC0jFYmRNXbAf',
    '_qimei_fingerprint': 'ed0574d6fbc29ee757df6d343e705fa1',
    'ptui_loginuin': '1758454412',
    'wr_vid': '384303150',
    'wr_rt': 'web%40yuT46OgYkHjL4fefOI1_AL',
    'uin': 'o1758454412',
    'skey': '@NsLwtXrpH',
    'wr_skey': 'x9eSTBe1',
    'wr_gid': '270606190',
    'wr_fp': '1514197865',
}


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=dev-1738835404736,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=089a84c4334d414c8dcd1528fe416a69',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://weread.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/2bb32ff0813ab6ffcg014315kb2e32a503132b2eb7349b01',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '089a84c4334d414c8dcd1528fe416a69-a42aaee216cd2543',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'ptcz=1cd2978655d7c327695ef59c013b4efa29dec9a37ce0a2bf336874962a7cc858; pgv_pvid=9291276337; o_cookie=1758454412; _qimei_q36=; LW_uid=l1N7v1y6A2E662f54733g3a2b6; LW_sid=w1I7w1g6I2x6R4o063I7k1Z1J3; _clck=1rg6idj|1|fn6|0; wr_localvid=aed32df0816e8002eaedf12; wr_name=%E6%96%BC%E6%98%AF%E6%8A%8A%E8%A9%A9%E6%91%BA%E7%96%8A; wr_avatar=https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0003-TmA2mZmwnna9IzVRHumimd8%2F0; eas_sid=r1Y772a2r8n2q7W035w0l2r6V9; qq_domain_video_guid_verify=f257275ca9c88543; RK=61fYOI4TFs; pac_uid=0_CC0jFYmRNXbAf; _qimei_h38=98e58604d3919694bd80bd760300000df1830d; wr_gender=1; wr_pf=NaN; suid=user_0_CC0jFYmRNXbAf; _qimei_fingerprint=ed0574d6fbc29ee757df6d343e705fa1; ptui_loginuin=1758454412; wr_vid=384303150; wr_rt=web%40yuT46OgYkHjL4fefOI1_AL; uin=o1758454412; skey=@NsLwtXrpH; wr_skey=x9eSTBe1; wr_gid=270606190; wr_fp=1514197865',
}


"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    'appId': 'wb115321887466h1205141645',
    'b': '2bb32ff0813ab6ffcg014315',
    'c': 'b2e32a503132b2eb7349b01',
    'ci': 88,
    'co': 5504,
    'sm': '民解放斗争。但是到了一九二七年春夏之交，',
    'pr': 70,
    'rt': 30,
    'ts': 1742183363473,
    'rn': 738,
    'sg': '4dcd71e0499d1a6789fbce24ec8d087bb76ab5bf000813fc6d3906f3b3822d7c',
    'ct': 1742183363,
    'ps': '49a32b907a625c2fg013801',
    'pc': '63c327c07a625c2fg014777',
}


def convert(curl_command):
    """提取bash接口中的headers与cookies"""
    headers = {}

    # 提取 headers
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers[match[0].strip()] = match[1].strip()

    # 提取 cookies（支持 -b 传递）
    cookies = {}
    cookie_match = re.search(r"-b '([^']+)'", curl_command)
    if cookie_match:
        cookie_string = cookie_match.group(1)
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key] = value

    return headers, cookies



# headers, cookies = convert(curl_str) if curl_str else (headers, cookies)

# Add read random time
READ_NUM += random.randint(10, 100)
