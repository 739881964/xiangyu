# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 11:31
# @Author  : Xiang Yu
# @File    : receive_send_serial.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import json
from time import sleep

import serial
# import serial.tools.list_ports
from scripts.pandas_manual import PandasManual


class OperationSerial:
    """ Python 使用串口接收和发送数据 """

    def __init__(self, port, _path, is_debug=True):
        if is_debug:
            self.port = serial.Serial(port, 115200)
        else:
            self.port = serial.Serial(port, 9600)
        self._path = _path
        if not self.port:
            self.port.open()

    def is_open(self):
        """ 打开串口 """
        if not self.port.is_open:
            self.port.open()

    def close_port(self):
        """ 关闭串口 """
        self.port.close()

    def read_debug_data(self):
        """ 接收串口数据 debug 模式 115200 baud"""
        data = str(self.port.readline().decode('utf8'))
        # data = str(self.port.readline(), 'utf8')
        with open(self._path, 'a+') as f:
            f.write(data + '\n')
            if 'SpottingWordList' in data:
                print(data)

    def read_com_data(self, excel_data):
        """ 接收串口数据 串口通讯模式 9600 baud """
        data = self.port.readline()
        if len(data) == 13:
            print(data)
            r = list(map(hex, list(data)))
            print(r)
            ret = r[-3:] + r[:-3]
            res = ' '.join(list(map(lambda y: y.replace('x', '').upper()[-2:], ret)))
            for excel in excel_data:
                if excel['语音模块发送给主控MCU的UART数据'] == res:
                    print(excel['命令 或 状态'])

            print(res)
            print()

    def send_data(self, data):
        """ 发送数据给串口 """
        # _data = ' '.join([hex(ord(c)).replace('0x', '') for c in data])
        _data = bytes.fromhex(data)
        if self.is_open():
            self.port.write(_data)
            print('串口码：{}  发送成功 ！！！'.format(_data))
        else:
            print(data)
            print('{}  发送失败......'.format(_data))


if __name__ == "__main__":
    path = r'C:\Users\xiangyu\xiangyu_git\work_directory\files\port_data'
    obj = OperationSerial('COM4', path, is_debug=True)
    panda = PandasManual(r'C:\Users\xiangyu\Desktop\PR-140-海邦照明灯控用户定制项目-方案规格书.xlsx')
    tara_data = panda.get_data('串口通信数据详表以及语音播报内容')['主控MCU发送给语音模块的UART数据'].tolist()
    all_data = panda.read_data('串口通信数据详表以及语音播报内容')

    while True:
        obj.read_debug_data()

    # for _one_data in tara_data:
    #     # _one_data = one_data[9:] + ' ' + one_data[:8]
    #     obj.send_data(_one_data)
    #     sleep(1)

        # while True:
        #     string = input('请输入(y/n) 继续？：')
        #     try:
        #         if string == 'y':
        #             pass
        #         elif string == 'n':
        #             break
        #         break
        #     except:
        #         print('请输入合法的选项')

