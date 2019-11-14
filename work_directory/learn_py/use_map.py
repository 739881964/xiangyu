# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 10:07
# @Author  : Xiang Yu
# @File    : use_map.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if self.name == other:
            return

    def __hash__(self):
        return hash(self.age)


a = Student('余翔', 24)
b = Student('余翔', 24)

print(Student.__dict__)
