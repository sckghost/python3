#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/5/5 15:51
# @Author  : SckGhost
# @File    : pachong.py
# @Software: PyCharm
import socket
import urllib.error
import urllib.parse
import urllib.request


data = bytes(urllib.parse.urlencode({'world!':'hello'}),encoding='utf-8')

# url= 'https://www.python.org'
url = 'http://httpbin.org/post'

try:
    response  =  urllib.request.urlopen(url,data=data,timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time Out')
print(response.read())
#
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


# print(response.read().decode('utf-8'))