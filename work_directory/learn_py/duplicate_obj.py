# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 11:44
# @Author  : Xiang Yu
# @File    : duplicate_obj.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


class People:
    """ 对象去重 """

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __eq__(self, other):
        if (self.name == other.name) and (self.gender == other.gender):
            return True
        return False

    def __hash__(self):
        return hash(self.name + self.gender)


a = People('余翔', 24, 'male')
b = People('余翔', 25, 'male')

print(set([a, b]))

