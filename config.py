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
    'ptui_loginuin': '1758454412',
    'wr_vid': '384303150',
    'wr_rt': 'web%40OxWwXFwMV79qLDpSpZP_AL',
    '_qimei_uuid42': '1931e0d1606100d65f1a1dd73709a6aa13cba47446',
    'fqm_pvqid': '2ad5a316-12b3-40ef-aa1c-0d66984c30fa',
    '_qimei_fingerprint': 'ed0574d6fbc29ee757df6d343e705fa1',
    'wr_fp': '3133900466',
    'wr_skey': 'VdBLdNnh',
    'wr_gid': '296997816',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=dev-1744355656859,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=f32f1124c94144d1a176785787286c89',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://weread.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/2bb32ff0813ab6ffcg014315k077323002f9077e29b114b2',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'f32f1124c94144d1a176785787286c89-99152f599ff0ce11',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'ptcz=1cd2978655d7c327695ef59c013b4efa29dec9a37ce0a2bf336874962a7cc858; pgv_pvid=9291276337; o_cookie=1758454412; _qimei_q36=; LW_uid=l1N7v1y6A2E662f54733g3a2b6; LW_sid=w1I7w1g6I2x6R4o063I7k1Z1J3; _clck=1rg6idj|1|fn6|0; wr_localvid=aed32df0816e8002eaedf12; wr_name=%E6%96%BC%E6%98%AF%E6%8A%8A%E8%A9%A9%E6%91%BA%E7%96%8A; wr_avatar=https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0003-TmA2mZmwnna9IzVRHumimd8%2F0; eas_sid=r1Y772a2r8n2q7W035w0l2r6V9; qq_domain_video_guid_verify=f257275ca9c88543; RK=61fYOI4TFs; pac_uid=0_CC0jFYmRNXbAf; _qimei_h38=98e58604d3919694bd80bd760300000df1830d; wr_gender=1; wr_pf=NaN; suid=user_0_CC0jFYmRNXbAf; ptui_loginuin=1758454412; wr_vid=384303150; wr_rt=web%40OxWwXFwMV79qLDpSpZP_AL; _qimei_uuid42=1931e0d1606100d65f1a1dd73709a6aa13cba47446; fqm_pvqid=2ad5a316-12b3-40ef-aa1c-0d66984c30fa; _qimei_fingerprint=ed0574d6fbc29ee757df6d343e705fa1; wr_fp=3133900466; wr_skey=VdBLdNnh; wr_gid=296997816',
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
    'c': '077323002f9077e29b114b2',
    'ci': 31,
    'co': 338,
    'sm': '论持久战[插图]（一九三八年五月）问题的',
    'pr': 28,
    'rt': 30,
    'ts': 1744855492950,
    'rn': 254,
    'sg': '961fe1a54080710425fe55a46a7b47f7c46182c4c7b58a95ba1b0d1d980e1040',
    'ct': 1744855492,
    'ps': '5fb323707a667026g019992',
    'pc': '0c232c407a667027g010adc',
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
