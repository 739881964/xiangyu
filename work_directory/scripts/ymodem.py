# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 16:30
# @Author  : Xiang Yu
# @File    : ymodem.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import serial
import time
import os
from sys import argv
from binascii import b2a_hex, a2b_hex

BAUDRATE = 9600
TIMEOUT = 0.05
BLOCKSIZE = 512


def readfile(filename, readLen):
    dataList = []

    fileSize = os.path.getsize(filename)
    blockNum = fileSize / readLen
    if fileSize % readLen != 0:
        blockNum += 1
    print("size %d, blockNum %d" % (fileSize, blockNum))

    with open(filename, 'rb') as f:
        for i in range(blockNum):
            block = f.read(readLen)
            dataList.append(block.strip())
    f.close()
    return dataList, blockNum


def sendCommandToDevice(COMx, cmdStr, expectedAck, TryTime):
    ack = 'no'
    for i in range(TryTime):
        num = COMx.write(cmdStr)
        ack = COMx.read(32)
        # print 'COM recv:%s' % ack
        if ack == expectedAck:
            break
    return ack


if __name__ == "__main__":

    portNum = argv
    port = "COM%s" % portNum

    FWUP_START = "AT+&UPDM=1\r\n\r\n"
    FWUP_TRANS = "AT+&UPDD=512\r\n"
    FWUP_END = "AT+&UPDM=0\r\n\r\n"
    START_OK = '+OK\r\n\r\n'
    TRANS_OK = '+OK=1\r\n\r\n'
    SET_OK = '+OK=-1\r\n\r\n'

    fwBlocks, blockNum = readfile(r"C:\Users\xiangyu\Desktop\test_res\20191120-release_1.0.14_00.4-8009735\package\app_iet_upgrade.bin", BLOCKSIZE)
    '''
    for i in range(blockNum):
        print 'fwBlocks[%d]:%d' % (i,len(fwBlocks[i]))
    '''

    try:
        COM = serial.Serial(port, BAUDRATE, timeout=TIMEOUT)

        for i in range(0, blockNum, 1):
            response = sendCommandToDevice(COM, FWUP_START, START_OK, 5)
            if response == START_OK:
                response = sendCommandToDevice(COM, FWUP_TRANS, SET_OK, 5)
                if response == SET_OK:
                    response = sendCommandToDevice(COM, fwBlocks[i], TRANS_OK, 5)
                    if response == TRANS_OK:
                        print("fwBlocks[%d] OK" % i)
                    else:
                        print("fwBlocks[%d] Fail" % i)
                        # i -= 1;

        response = sendCommandToDevice(COM, FWUP_END, START_OK, 5)
        if START_OK == response:
            print("set OK")
        else:
            print('set Fail')
        COM.close()
        print('Steps over, COM close.')
    except Exception as e:
        print('%s:' % str(Exception))
        print('%s:' % str(e))


# from ctypes import *
#
# dll = windll.LoadLibrary("PCOMM.DLL")
#
# port = 10  # 指定串口COM2
#
# dll.sio_open(port)
#
# dll.sio_ioctl(port, 15, 0x00 | 0x03 | 0x00)  # 57600, 无校验，8位数据位，1位停止位
#
#
# def cb(xmitlen, buflen, pbuf, flen):
#     print(xmitlen, flen,)
#     print()
#     return xmitlen
#
#
# CALLBACK = WINFUNCTYPE(c_int, c_long, c_int, POINTER(c_char), c_long)
#
# ccb = CALLBACK(cb)
#
# dll.sio_FtYmodemTx(port, "e:\test.jpg", ccb, 0)
#
# dll.sio_close(port)

