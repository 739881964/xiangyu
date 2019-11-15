# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 13:49
# @Author  : Xiang Yu
# @File    : new_serial.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import serial
from time import sleep


sr = serial.Serial('COM10', '9600')
data = '5A 01 0A 07 00 1E 00 00 00 00 00 48 0D'
sr.write(bytes.fromhex(data))
sr.close()

