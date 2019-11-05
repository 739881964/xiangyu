# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 13:43
# @Author  : Xiang Yu
# @File    : grep_rereticle.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


def find_str(a_str):
    re_string = a_str[::-1]  # 反向输出 a_str
    print(a_str)
    print(re_string)
    for l in range(len(a_str)):
        if a_str[l] == 0:
            pass


string = 'asbccbas'
find_str(string)


a = len(string)
i = 0
count = 1
while i <= (a/2):
    if string[i] == string[a-i-1]:  #
        count = 1
        i += 1
    else:
        count = 0
        break

if count == 1:
    print('您所输入的字符串是回文')
else:
    print('您所输入的字符串不是回文')