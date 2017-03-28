# !/usr/bin/evn python3
# -*- coding: utf-8 -*-

# 利用gunicorn启动本地服务器命令   gunicorn httpbin:app
# 可通过127.0.0.1:8000 访问

import urllib.request
import urllib3
from urllib import parse
import requests

def use_simple_urllib(url_ip):
    response = urllib.request.urlopen(url_ip)
    # print(response.headers) <==> print(response.info())
    print(response.info())
    for line in response.readlines():
        print(line)

def use_simple_urllib2(url_ip):
    # 构建请求参数
    dic = {'name':'jack','age':100}

    # urlencode函数把字典化为字符串
    params = urllib.parse.urlencode(dic)
    # print(type(params)) str
    # 发送请求
    # join函数是通过特定字符串把数组里的字符串连接起来
    url = '?'.join([url_ip,params])
    print('url is ',url)
    response = urllib.request.urlopen(url)
    if response.getcode() == 200:
        print(response.info())
        for line in response.readlines():
            print(line)


# requests
# 支持更多Encoding格式
# 支持多次请求一个连接
def use_simple_requests(url_ip):
    params = {'name': 'jack', 'age': 100}
    # 发送请求
    response = requests.get(url_ip,params=params)
    print(response.text)
    print(response.status_code)
    print(response.json())
    print(response.headers)

if __name__ == '__main__':
    url_ip = 'http://127.0.0.1:8000/get'
    # use_simple_urllib(url_ip)
    # use_simple_urllib2(url_ip)
    use_simple_requests(url_ip)
