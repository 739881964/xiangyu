# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 16:30
# @Author  : Xiang Yu
# @File    : ymodem.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import os
import struct
from ctypes import *

dll = windll.LoadLibrary("PCOMM.DLL")

port = 4  # 指定串口COM2

dll.sio_open(port)

dll.sio_ioctl(port, 16, 0x00 | 0x03 | 0x00)  # 115200, 无校验，8位数据位，1位停止位


def cb(xmitlen, buflen, pbuf, flen):
    print(xmitlen, flen,)
    print()
    return xmitlen


CALLBACK = WINFUNCTYPE(c_int, c_long, c_int, POINTER(c_char), c_long)

ccb = CALLBACK(cb)

path = r'C:\Users\xiangyu\Desktop\test_res\20191120-release_1.0.14_00.4-8009735\package'
all_bin = os.listdir(path)
for _bin in all_bin:
    if 'bin' in _bin:
        whole_bin = os.path.join(path, _bin)
        dll.sio_FtYmodemTx(port, whole_bin, ccb, 0)
        print(ccb)
        print('%s 烧录完成 ！' % _bin)
print('烧录完成！！！')

dll.sio_close(port)

