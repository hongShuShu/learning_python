# !usr/bin/evn python3
# -*- coding:utf-8 -*-
# http://www.imooc.com/video/13160

import requests
import json

# github-token:setting->personAccessTokens->user
token = 'b2e3747945f1c31a3cdd10852d615ee98d5766b7'
BASE_URL = 'https://api.github.com'
authorize = 'token '.join(['', token])

def build_url(end_point):
    return '/'.join([BASE_URL,end_point])

def my_print(json_str):
    # indent缩进4
    print(json.dumps(json.loads(json_str),indent=4))

# 基本认证
def basic_auth():
    response = requests.get(build_url('users'),auth=('hongShuShu','密码'))
    my_print(response.text)
    print(response.request.headers)

# OAUTH
def basic_oauth():
    headers = {'Authorization':authorize}
    # user/emails
    response = requests.get(build_url('user/emails'),headers=headers)
    my_print(response.text)
    print(response.request.headers)


from requests.auth import AuthBase


class GitHubAuth(AuthBase):
    def __init__(self,token):
        self.token = token

    def __call__(self, res):
        # requests 加headers
        res.headers['Authorization'] = authorize
        return res

def oauth_advanced():
    auth = GitHubAuth(token)
    response = requests.get(build_url('user/emails'),auth=auth)
    my_print(response.text)

# basic_auth()
# basic_oauth()
oauth_advanced()