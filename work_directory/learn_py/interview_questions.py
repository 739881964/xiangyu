# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 15:08
# @Author  : Xiang Yu
# @File    : interview_questions.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


def find_num(num, array):
    if num in array:
        print('{} 存在于 {}'.format(num, array))
    else:
        print('{} 不存在于 {}'.format(num, array))


n = 7
arr = [1, 3, 5, 2]
find_num(n, arr)


def show_num(a, array):
    x = 0
    for num in array:
        if (num % 3 == 0) or (num % 5 == 0):
            print(num, end=' ')
            x += 1
            if x >= a:
                x = 0
                print()


show_num(8, range(1, 101))
