# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 11:35
# @Author  : Xiang Yu
# @File    : dic_content.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


"""
编程题：给定一个正整数列表，请你排列他们，使他们成为最大的数字。
例如：给定[6,30,32,7,9],最大的形成的数字是9763230.(提示：结果可能特别大，所以你要返回一个字符串，而不是一个整数)
请你用熟悉的语言实现。
"""

import random


def search_item_from_array(array, value):
    if len(array) == 0:
        return -1

    index = len(array) - 1
    first_value = array[0]

    if first_value == value:
        # 如果第一个元素等于查找值，直接返回
        return 0

    # 把要查找的值放在数组的第一位上，作为【标兵】
    array[0] = value
    while array[index] != value:
        index -= 1

    # 查找结束，把数组的首位元素改回来
    array[0] = first_value

    return index if(index > 0) else -1


def get_sorted(a_list: list) -> list:
    len_a = len(a_list)
    for i in range(len_a):
        for j in range(i - 1):
            if a_list[i] > a_list[j]:
                a_list[j], a_list[i] = a_list[i], a_list[j]

    return a_list


def get_num(a_list: list) -> tuple:
    s_ten_list = list(filter(lambda x: x < 10, a_list))
    o_list = list(filter(lambda y: y not in s_ten_list, a_list))
    # for i in range(10):
    #     for j in a_list:
    #         pass
    return o_list, s_ten_list


def get_random_list():
    return random.sample(range(600, 800, 10), 3)


if __name__ == '__main__':
    example = [6, 30, 32, 7, 9]
    res = get_sorted(example)
    # print(res)
    r = get_num(res)
    # print(r)


    one_list = get_random_list()
    user_data = [one_list]
    # print(user_data)

    a_list = []
    it = None
    search_item_from_array(a_list, it)

