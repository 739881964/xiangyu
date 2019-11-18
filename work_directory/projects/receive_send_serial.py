# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 11:31
# @Author  : Xiang Yu
# @File    : receive_send_serial.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


__all__ = ["PandasManual", "OperationSerial", 'main']


import sys
import os
import time

import serial
import pandas as pd
from openpyxl import load_workbook, Workbook


class PandasManual:
    """ pandas operate excel """

    def __new__(cls, *args, **kwargs):
        """ only create one object address """
        if not hasattr(PandasManual, '_instance'):
            cls._instance = super(PandasManual, cls).__new__(cls)

            return cls._instance

    def __init__(self, file_path):
        # super().__init__(file_path)
        self.file_path = file_path
        self.sheet_name = []

    def read_csv(self, sheet: 'data -> str' = None, encoding: 'format type' = 'gbk'):
        """ read csv file content """
        data = None
        try:
            if sheet:
                data = pd.read_csv(self.file_path, sheet_name=sheet, encoding=encoding)
            else:
                data = pd.read_csv(self.file_path, encoding=encoding)
        except Exception as e:
            print(e)
            # raise e

        return data

    def get_data(self, sheet=''):
        """ read excel whole data by pandas"""
        if sheet:
            data = pd.read_excel(self.file_path, sheet_name=sheet)
        else:
            data = pd.read_excel(self.file_path, sheet_name=self.sheet_name[1])

        return data

    def read_data(self, sheet='') -> list:
        """
        read excel file by openpyxl
        return: content is dict-list
        """
        wb = load_workbook(self.file_path)
        if sheet:
            sheet = wb[sheet]
        else:
            sheet = wb[self.sheet_name[1]]
        head_data = list(sheet.iter_rows(max_row=2, values_only=True))[0]

        data_list = list()
        for data in list(sheet.iter_rows(min_row=2, max_row=sheet.max_row, values_only=True)):
            dic = dict(zip(head_data, data))
            data_list.append(dic)

        return data_list

    # @run_time(2)
    def write_data(self, rows: list, columns: list, res: list, sheet=None):
        """
        write in excel depend on row by openpyxl
        """
        wb = load_workbook(self.file_path)
        if sheet:
            sheet = wb[sheet]
        else:
            sheet = Workbook().create_sheet('pass_fail_info')

        for row in rows:
            if isinstance(row, int) and 2 <= row <= sheet.max_row:
                for col in columns:
                    try:
                        sheet.cell(row, col).value = res[col]
                        wb.save(self.file_path)
                    except Exception as e:
                        print("write in Excel failed")
                        # raise e
            else:
                print('row is not exist')

    # @run_time(2)
    def excel_add_sheet(self, data: list, sheet: list, _sheet_name='首页', header=None, index=None):
        """ not kill before operation when write after depend on column by pandas"""
        # if not exists excel txt, then create it
        try:
            if not os.path.exists(self.file_path):
                df = pd.DataFrame(['测试结果已生成!'])
                df.to_excel(self.file_path, sheet_name=_sheet_name, header=header, index=index)
                print('创建测试结果文件xlsx成功！')
        except (FileExistsError, Exception) as e:
            print(f'xlsx测试结果文件已存在，自动创建失败-{e}')
            raise e

        with pd.ExcelWriter(self.file_path) as excel_writer:
            book = load_workbook(excel_writer.path)
            excel_writer.book = book

            for i in range(len(data)):
                self.sheet_name.append(sheet[i])
                df = pd.DataFrame(data[i])
                df.to_excel(excel_writer=excel_writer, sheet_name=sheet[i], index=False)

            excel_writer.save()
        # excel_writer.close()


class OperationSerial:
    """ 实现串口与主控MCU之间的通信：数据接收与发送 """

    def __init__(self, port, is_debug=False):
        """ 初始化连接串口，接收端口和波特率，一般为：9600 或 115200 """
        if is_debug:
            self.port = serial.Serial(port, 115200)
        else:
            self.port = serial.Serial(port, 9600)
        if not self.port:
            self.port.open()

    def is_open(self):
        """ 打开串口 """
        if not self.port.is_open:
            self.port.open()

    def close_port(self):
        """ 关闭串口 """
        self.port.close()

    def debug(self):
        """
        接收串口数据 debug 模式 115200 波特率
        :return: None
        """
        while True:
            data = str(self.port.readline().decode('utf8'))
            # data = str(self.port.read(byte).decode('utf8'))  # decode('utf8'))
            # data = str(self.port.readline(), 'utf8')
            # with open(self._path, 'a+') as f:
            #     f.write(data + '\n')
            # if 'SpottingWordList' in data:
            print(data)

    def receive(self, byte: int, excel_data: list):
        """
        接收串口数据 串口通讯模式 9600 波特率
        :param byte: 接收的字节数
        :param excel_data: excel读取的嵌套字典数据
        :return: None
        """
        while True:
            data = self.port.read(byte)
            # print(data)
            # if len(data) == 13:
            if data:
                r = list(map(hex, list(data)))
                # print(r)
                # ret = r[-3:] + r[:-3]
                res = ' '.join(list(map(lambda y: y.replace('x', '').upper()[-2:], r)))
                for excel in excel_data:
                    if excel['语音模块发送给主控MCU的UART数据'] == res:
                        print('响应串口码: [{}] -> 对应的命令或状态：[{}]'.format(res, excel['命令 或 状态']))
                        break
                else:
                    print('响应的串口码 [{}] 无法在excel中找到'.format(res))

                # print(res)
                print()

    def send(self, serial_data: list, comm_data: list):
        """
        发送数据给串口 串口通讯模式 9600 波特率
        :param serial_data: 发送的串口数据
        :param comm_data: 命令或状态词
        :return: None
        """
        # _data = ' '.join([hex(ord(c)).replace('0x', '') for c in data])
        for i in range(len(serial_data)):
            one_data = serial_data[i]
            _data = bytes.fromhex(one_data)
            try:
                self.port.write(_data)
                print('命令或状态: [{}] 串口码：[{}] -> 发送成功 '.format(comm_data[i], one_data))
                while True:
                    result = input('请输入语音反馈是否正确(y/n/q?)： ')
                    try:
                        if (result == 'y') or (result == 'Y'):
                            print('发送串口码 [{}] -> MCU -> 语音响应成功'.format(one_data))
                            break
                        elif (result == 'n') or (result == 'N'):
                            print('发送串口码 [{}] -> MCU -> 语音响应错误'.format(one_data))
                            break
                        elif (result == 'q') or (result == 'Q'):
                            return
                    except:
                        print('请输入合法的测试结果(y/n/q?)')
            except:
                print('命令或状态: [{}] 串口码：[{}] -> 发送失败 '.format(comm_data[i], one_data))
            print()

    def receive_and_send(self, byte: int, dic_data: list, sleep_time: int, cmd_data: list):
        """
        接收串口数据并点发送excel中相应的串口数据
        :param byte: 接收串口字节数
        :param dic_data: 读取的excel数据
        :param sleep_time: 识别与发送串口码的间隔时间
        :param cmd_data: 命令或状态词
        :return: None
        """
        while True:
            data = self.port.read(byte)
            if data:
                r = list(map(hex, list(data)))
                # print(r)
                # ret = r[-3:] + r[:-3]
                res = ' '.join(list(map(lambda y: y.replace('x', '').upper()[-2:], r)))
                for i in range(len(dic_data)):
                    if dic_data[i]['语音模块发送给主控MCU的UART数据'] == res:
                        print('响应的串口码: [{}] -> 命令或状态：[{}]'.format(res, dic_data[i]['命令 或 状态']))
                        time.sleep(sleep_time)
                        one_data = dic_data[i]['主控MCU发送给语音模块的UART数据']
                        _data = bytes.fromhex(one_data)
                        try:
                            self.port.write(_data)
                            print('命令或状态: [{}] -> 发给主控MCU串口码：[{}] -> 发送成功 '.format(cmd_data[i], one_data))
                            while True:
                                result = input('请输入语音反馈是否正确(y/n/q?)： ')
                                try:
                                    if result == 'y':
                                        print('发送串口码 [{}] -> MCU -> 语音响应成功'.format(one_data))
                                        break
                                    elif result == 'n':
                                        print('发送串口码 [{}] -> MCU -> 语音响应错误'.format(one_data))
                                        break
                                except:
                                    print('请输入合法的测试结果(y/n/q?)')
                        except:
                            print('命令或状态: [{}] 串口码：[{}] -> 发送失败 '.format(dic_data[i]['命令 或 状态'], one_data))
                        break
                else:
                    print('响应的串口码 [{}] 无法在excel中找到'.format(res))
                print()


def main(r_data, t_data, c_data, port: '端口号', model: '选择模式', recv_bytes: int, sp_time: int):
    """
    根据需要选择测试的模式
    :param r_data: excel预期接收到的串口码
    :param t_data: excel发送给主控MCU的串口码
    :param c_data: 命令或状态词
    :param port: 设备连接的端口号
    :param model: 测试模式
    :param recv_bytes: 接收串口数据字节数
    :param sp_time: 接收串口数据与发送串口数据之间的间隔时间
    :return: None
    """
    if model == 'SPD':
        # debug模式
        obj = OperationSerial(port, is_debug=True)
        obj.debug()
    elif model == 'SPR':
        # 串口通讯接收模式
        obj = OperationSerial(port)
        obj.receive(recv_bytes, r_data)
    elif model == 'SPS':
        # 串口通讯发送模式
        obj = OperationSerial(port)
        obj.send(t_data, c_data)
    elif model == 'SPT':
        # 串口通讯接收与发送模式
        obj = OperationSerial(port)
        obj.receive_and_send(recv_bytes, r_data, sp_time, c_data)


if __name__ == "__main__":
    try:
        panda = PandasManual(r'C:\Users\xiangyu\Desktop\串口数据.xlsx')
        tara_data = panda.get_data('串口通信数据详表以及语音播报内容')['主控MCU发送给语音模块的UART数据'].tolist()
        command_data = panda.get_data('串口通信数据详表以及语音播报内容')['命令 或 状态'].tolist()
        all_data = panda.read_data('串口通信数据详表以及语音播报内容')
    except:
        print('获取excel数据失败')
        sys.exit()
    else:
        # 根据项目需求：输入端口、模式、接收字节数、接收与发送数据的时间间隔参数
        main(all_data, tara_data, command_data, port='COM10', model='SPR', recv_bytes=13, sp_time=3)
    finally:
        print()
        print('Test End !')

