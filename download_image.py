# !usr/bin/evn python3
# -*- coding:utf-8 -*-

import requests

def download_photo():
    '''下载图片'''
    UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    headers = {'User-Agent':UserAgent}
    url = 'http://img3.imgtn.bdimg.com/it/u=2228635891,3833788938&fm=21&gp=0.jpg'
    # 加上headers模拟正常请求 stream支持流传输
    res = requests.get(url,headers=headers,stream=True)
    print(res.status_code,res.reason)
    print(res.request.headers)

    # 以二进制写模式打开
    with open('github.jpg','wb') as fd:
        for chunk in res.iter_content(128):
            # 一块一块的写入fd地址所对应的文件
            fd.write(chunk)


def readModel():
    print('读写方式')
    # w 以写方式打开(必要时清空)
    # a 以追加模式打开(从EOF开始, 必要时创建新文件)
    # r+ 以读写模式打开
    # w+ 以读写模式打开(参见w)
    # a+ 以读写模式打开(参见a)
    # rb 以二进制读模式打开
    # wb 以二进制写模式打开(参见w)
    # ab 以二进制追加模式打开(参见a)
    # ab+ 以二进制读写模式打开(参见a+)
    # rb+ 以二进制读写模式打开(参见r+)
    # wb+ 以二进制读写模式打开(参见w+)


def download_photo_improverd():
    UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    headers = {'User-Agent': UserAgent}
    url = 'http://img3.imgtn.bdimg.com/it/u=2228635891,3833788938&fm=21&gp=0.jpg'
    # 加上headers模拟正常请求 stream支持流传输
    res = requests.get(url, headers=headers, stream=True)
    from contextlib import closing
    with closing(requests.get(url,headers=headers,stream=True)) as response:
        ''' 打开文件 with可以很好的处理上下文环境产生的异常
        紧跟with后面的语句被求值后，返回对象的 __enter__() 方法被调用，
        这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，
        将调用前面返回对象的 __exit__()方法。'''
        with open('github1.png','wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__ == '__main__':
    # download_photo()
    download_photo_improverd()