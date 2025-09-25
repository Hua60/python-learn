from http.client import responses

import requests

url = "http://172.16.1.11/"

data = {
    "callback": "dr1003",
    "DDDDD": "20250702002@telecom",
    "upass": "zzx104275",
    "0MKKey": "123456",
    "R1": "0",
    "R2": "",
    "R3": "0",
    "R6": "0",
    "para": "00",
    "v6ip":"",
    "terminal_type": "1",
    "lang": "zh-cn",
    "jsVersion": "4.1.3",
    "v": "1008",
}

header = {
"Accept":"*/*",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Connection":"keep-alive",
"Host":"172.16.1.11",
"Referer":"http://172.16.1.11/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.242.400 QQBrowser/19.6.6737.400"
}

response = requests.post(url, data, headers=header).status_code
print("回应代码{}".format(response))