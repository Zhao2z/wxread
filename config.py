# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认40次/20分钟
READ_NUM = int(os.getenv('READ_NUM') or 50)
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
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    'uin': 'o1758454412',
    'skey': '@NMrz1VLNz',
    'RK': 'Q8fYKI4bWu',
    'ptcz': '70454c14a042a16bd5ef093d8feba0d89bab1c440f7bd46e71cca66e69f5be0f',
    'wr_gid': '260711347',
    'wr_fp': '3133900466',
    'wr_vid': '384303150',
    'wr_rt': 'web%40wuzgICBnsVmvgJb~SRT_AL',
    'wr_localvid': 'aed32df0816e8002eaedf12',
    'wr_name': '%E6%96%BC%E6%98%AF%E6%8A%8A%E8%A9%A9%E6%91%BA%E7%96%8A',
    'wr_avatar': 'https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0003-TmA2mZmwnna9IzVRHumimd8%2F0',
    'wr_gender': '1',
    'wr_pf': 'NaN',
    'wr_skey': 'P9k1Osn2',
}


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=dev-1745492224532,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=b9881de547764be186db6bb16f432402',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://weread.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/2bb32ff0813ab6ffcg014315',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'b9881de547764be186db6bb16f432402-a50376c8a78435d0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'uin=o1758454412; skey=@NMrz1VLNz; RK=Q8fYKI4bWu; ptcz=70454c14a042a16bd5ef093d8feba0d89bab1c440f7bd46e71cca66e69f5be0f; wr_gid=260711347; wr_fp=3133900466; wr_vid=384303150; wr_rt=web%40wuzgICBnsVmvgJb~SRT_AL; wr_localvid=aed32df0816e8002eaedf12; wr_name=%E6%96%BC%E6%98%AF%E6%8A%8A%E8%A9%A9%E6%91%BA%E7%96%8A; wr_avatar=https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0003-TmA2mZmwnna9IzVRHumimd8%2F0; wr_gender=1; wr_pf=NaN; wr_skey=P9k1Osn2',
}

# 书籍
book = [
    "2bb32ff0813ab6ffcg014315","6f932ec05dd9eb6f96f14b9","43f3229071984b9343f04a4","d7732ea0813ab7d58g0184b8",
    "3d03298058a9443d052d409","4fc328a0729350754fc56d4","a743220058a92aa746632c0","140329d0716ce81f140468e",
    "1d9321c0718ff5e11d9afe8","ff132750727dc0f6ff1f7b5","e8532a40719c4eb7e851cbe","9b13257072562b5c9b1c8d6"
]

# 章节
chapter = [
    "2bb32ff0813ab6ffcg014315","a87322c014a87ff679a21ea","e4d32d5015e4da3b7fbb1fa","16732dc0161679091c5aeb1",
    "8f132430178f14e45fce0f7","c9f326d018c9f0f895fb5e4","45c322601945c48cce2e120","d3d322001ad3d9446802347",
    "65132ca01b6512bd43d90e3","c20321001cc20ad4d76f5ae","c51323901dc51ce410c121b","aab325601eaab3238922e53",
    "9bf32f301f9bf31c7ff0a60","c7432af0210c74d97b01b1c","70e32fb021170efdf2eca12","6f4322302126f4922f45dec"
]

"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    'appId': 'wb115321887466h725297694',
    'b': '2bb32ff0813ab6ffcg014315',
    'c': '6c9325802fa6c9882bbaddf',
    'ci': 32,
    'co': 5138,
    'sm': '照顾全局，照顾多数及和同盟者一道工作共产',
    'pr': 35,
    'rt': 30,
    'ts': 1745674714891,
    'rn': 529,
    'sg': '9980200f20285e5c644884f6e19751afc03df878d9afd88d89eaaec0dd4ba583',
    'ct': 1745674714,
    'ps': '73732fc07a67b026g0129ee',
    'pc': '73732fc07a67b026g0129ee',
    's': '6fb358a1',
}


def convert(curl_command):
    """提取bash接口中的headers与cookies
    支持 -H 'Cookie: xxx' 和 -b 'xxx' 两种方式的cookie提取
    """
    # 提取 headers
    headers_temp = {}
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers_temp[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    
    # 从 -H 'Cookie: xxx' 提取
    cookie_header = next((v for k, v in headers_temp.items() 
                         if k.lower() == 'cookie'), '')
    
    # 从 -b 'xxx' 提取
    cookie_b = re.search(r"-b '([^']+)'", curl_command)
    cookie_string = cookie_b.group(1) if cookie_b else cookie_header
    
    # 解析 cookie 字符串
    if cookie_string:
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key.strip()] = value.strip()
    
    # 移除 headers 中的 Cookie/cookie
    headers = {k: v for k, v in headers_temp.items() 
              if k.lower() != 'cookie'}

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
