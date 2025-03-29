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
    'wr_fp': '1514197865',
    'uin': 'o1758454412',
    'pgv_info': 'ssid=s7153118372',
    'skey': '@p0gMkOb2T',
    'rv2': '80519AF3F5DA373932D84AB0880CDF3802EE0E82BF6368084F',
    'property20': 'F1BCD66E0C8D1B3D691CC0B2851CCFF708F005A96AA748CAD07142684BCE180DFB33F94DAF574CD1',
    'wr_gid': '287159674',
    'wr_skey': 'zrnMNFx6',
    'wr_vid': '384303150',
    'wr_rt': 'web%40OxWwXFwMV79qLDpSpZP_AL',
}


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=dev-1743080809165,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=4b68ea9c4ecf40abb9fdd63e19634d31',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://weread.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/2bb32ff0813ab6ffcg014315k6c9325802fa6c9882bbaddf',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '4b68ea9c4ecf40abb9fdd63e19634d31-b7f93723f00dcda9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'ptcz=1cd2978655d7c327695ef59c013b4efa29dec9a37ce0a2bf336874962a7cc858; pgv_pvid=9291276337; o_cookie=1758454412; _qimei_q36=; LW_uid=l1N7v1y6A2E662f54733g3a2b6; LW_sid=w1I7w1g6I2x6R4o063I7k1Z1J3; _clck=1rg6idj|1|fn6|0; wr_localvid=aed32df0816e8002eaedf12; wr_name=%E6%96%BC%E6%98%AF%E6%8A%8A%E8%A9%A9%E6%91%BA%E7%96%8A; wr_avatar=https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0003-TmA2mZmwnna9IzVRHumimd8%2F0; eas_sid=r1Y772a2r8n2q7W035w0l2r6V9; qq_domain_video_guid_verify=f257275ca9c88543; RK=61fYOI4TFs; pac_uid=0_CC0jFYmRNXbAf; _qimei_h38=98e58604d3919694bd80bd760300000df1830d; wr_gender=1; wr_pf=NaN; suid=user_0_CC0jFYmRNXbAf; _qimei_fingerprint=ed0574d6fbc29ee757df6d343e705fa1; ptui_loginuin=1758454412; wr_fp=1514197865; uin=o1758454412; pgv_info=ssid=s7153118372; skey=@p0gMkOb2T; rv2=80519AF3F5DA373932D84AB0880CDF3802EE0E82BF6368084F; property20=F1BCD66E0C8D1B3D691CC0B2851CCFF708F005A96AA748CAD07142684BCE180DFB33F94DAF574CD1; wr_gid=287159674; wr_skey=zrnMNFx6; wr_vid=384303150; wr_rt=web%40OxWwXFwMV79qLDpSpZP_AL',
}


"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    'appId': 'wb115321887466h1205141645',
    'b': '2bb32ff0813ab6ffcg014315',
    'c': '6c9325802fa6c9882bbaddf',
    'ci': 32,
    'co': 338,
    'sm': '中国共产党在民族战争中的地位[插图]（一',
    'pr': 34,
    'rt': 30,
    'ts': 1743258460940,
    'rn': 989,
    'sg': '3412622f1a523e45aa0c7c20893f0f24543607830528e7a22b679d561a964d77',
    'ct': 1743258460,
    'ps': 'b5932ab07a64004ag010cbb',
    'pc': '0ae323707a64004ag0116f4',
}


# def convert(curl_command):
#     """提取bash接口中的headers与cookies"""
#     headers = {}

#     # 提取 headers
#     for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
#         headers[match[0].strip()] = match[1].strip()

#     # 提取 cookies（支持 -b 传递）
#     cookies = {}
#     cookie_match = re.search(r"-b '([^']+)'", curl_command)
#     if cookie_match:
#         cookie_string = cookie_match.group(1)
#         for cookie in cookie_string.split('; '):
#             if '=' in cookie:
#                 key, value = cookie.split('=', 1)
#                 cookies[key] = value

#     return headers, cookies



# headers, cookies = convert(curl_str) if curl_str else (headers, cookies)

# Add read random time
READ_NUM += random.randint(10, 100)
