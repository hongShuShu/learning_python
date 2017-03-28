# !/usr/bin/evn python3
# -*- coding: utf-8 -*-
# http://www.imooc.com/video/13160

import json
import requests
from requests import exceptions
import logging

def build_url(URL,endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    # indent缩进4
    return json.dumps(json.loads(json_str),indent=4)

def request_method(URL):
    url = build_url(URL,'users/hongShuShu')
    response = requests.get(url)
    print(better_print(response.text))

def params_request(URL):
    response = requests.get(build_url(URL,'users'),params={'since':11})
    print(better_print(response.text))

def patch_request(URL):
    url = build_url(URL,'user')
    # 可修改GitHub自己的信息
    response = requests.patch(url,auth=('hongShuShu','密码'),json={'location':'北京市海淀区'})
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

def timeout_request(URL):
    url = build_url(URL, 'user/emails')
    try:
        response = requests.get(url,timeout=0.1)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(e.args)
        logging.error(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        print(better_print(response.text))
        print(response.status_code)

# 自定义请求
def hard_requsts(URL):
    from requests import Request,Session
    s = Session()
    headers = {'User-Agent':'iPhone 10.2'}
    req = Request('GET',build_url(URL,'user/emails'),auth=('hongShuShu','密码'),headers=headers)
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)

    response = s.send(prepped,timeout=5)
    print(response.status_code)
    print(response.request.headers)
    print(response.text)

def response_params():
    res = requests.get('https://www.github.com')
    # dir函数可以查看该对象的所有方法
    print(dir(res))
    print(res.request)
    print(res.request.headers)
    print(res.content)
    print(res.text)
    print(res.json)
    # 查看响应时间
    print(res.elapsed)

if __name__ == '__main__':
    URL = 'https://api.github.com'
    # request_method(URL)
    # params_request(URL)
    # patch_request(URL)

    # timeout_request(URL)
    # hard_requsts(URL)
    response_params()