# !/usr/bin/evn python3
# _*_ coding:utf-8 _*_

import json
import requests

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
    response = requests.patch(url,auth=('hongShuShu','密码'),json={'location':'北京市海淀区'})

    print(better_print(response.text))

if __name__ == '__main__':
    URL = 'https://api.github.com'
    # request_method(URL)
    # params_request(URL)
    patch_request(URL)