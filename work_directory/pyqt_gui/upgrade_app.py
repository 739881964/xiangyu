# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 10:44
# @Author  : Xiang Yu
# @File    : upgrade_app.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import sys
import serial
import time
import numpy as np
import serial.tools.list_ports
import os
import struct
from ctypes import *
# from projects.receive_send_serial import OperationSerial


class ConnectSerial:
    """ 连接串口设备 """
    def __init__(self, port, baud, time_out=5):
        self.baud = baud
        self._port = port
        self.port = serial.Serial(self._port, self.baud, timeout=time_out)

        if not self.port:
            self.port.open()


class UpGrade(ConnectSerial):
    """ 升级版本 """

    def __init__(self, port='', baud=None, time_out=5):
        super(UpGrade, self).__init__(port, baud, time_out)

    @classmethod
    def get_port_list(cls):
        # 获取windows所有端口
        port_list = serial.tools.list_ports.comports()
        all_port = []
        for port in port_list:
            all_port.append(port[0])

        return all_port

    def write_data(self):
        # while True:
        # self.port.write(bytes(' \n', encoding='utf8') + b'\r')
        # print(bytes(' ', encoding='gbk') + b'\r')
        # time.sleep(1)
        # string = str(self.port.read_all().decode('utf8'))
        # if 'IET>' in string:
        self.port.write(bytes('flash -u\n', encoding='utf8') + b'\r')
        time.sleep(1)
        self.port.close()
        time.sleep(5)

        # print(type(string))
        # ret = self.port.readline().decode('utf8')
        # print(ret)


def cb(xmitlen, flen):
    print(xmitlen, flen, )
    print()
    return xmitlen


def re_connect(path):
    dll = windll.LoadLibrary("PCOMM.DLL")
    _port = 'COM4'
    _baud = 115200

    # while True:
    #     port = serial.Serial(_port, _baud, timeout=5)
    #     if port.is_open:
    #         break
    #     else:
    #         print("正在连接设备......")
    # port = serial.Serial(_port, _baud, timeout=5)
    res = input('Please reset/reconnect board first, then press [OK]' 'Tips: ')
    res = res.upper()

    port = serial.Serial(_port, _baud, timeout=5)
    if port:
        print('success')

    # while True:
    #     port = serial.Serial(_port, _baud, timeout=5)
    #     if port.is_open:
    #         break
    #     else:
    #         print("正在连接设备......")
    if res == "OK":
        time.sleep(1)
        port.write(bytes('upgrade -u\n', encoding='utf8') + b'\r')
        while True:
            string = str(port.read_all().decode('utf8'))
            print(string)
            if string:
                print(string)
                break
        if 'CCCC' in string:
            print(string)
            # self.port = serial.Serial(self._port, self.baud, timeout=5)
            # dll.sio_open(_port)
            # dll.sio_ioctl(_port, 16, 0x00 | 0x03 | 0x00)  # 115200, 无校验，8位数据位，1位停止位
            # CALLBACK = WINFUNCTYPE(c_int, c_long, c_int, POINTER(c_char), c_long)
            # ccb = CALLBACK(cb)
            # all_bin = os.listdir(path)
            # for _bin in all_bin:
            #     if 'bin' in _bin:
            #         whole_bin = os.path.join(path, _bin)
            #         dll.sio_FtYmodemTx(_port, whole_bin, ccb, 0)
            #         # print(ccb)
            #         print('%s 烧录完成 ！' % _bin)
            # print('烧录完成！！！')
    else:
        print('res is not equal OK !')
        sys.exit()


if __name__ == "__main__":
    _path = r'C:\Users\xiangyu\Desktop\test_res\20191120-release_1.0.14_00.4-8009735\package'
    upgrade = UpGrade("COM4", 9600)
    # print(upgrade.get_port_list())
    # upgrade.write_data()
    re_connect(_path)
