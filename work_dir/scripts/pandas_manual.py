# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 10:07
# @Author  : Xiang Yu
# @File    : pandas_manual.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import pandas as pd
from scripts.base_path import EXCEL_PATH
from openpyxl import load_workbook


def get_data(file_path, sheet_name, **kw):
    """读取excel所有数据"""
    data = pd.read_excel(file_path, sheet_name=sheet_name, **kw)
    return data


def write_data(data, file_path, sheet_name):
    """写入时参数需要传入一个list或者dict, 最后一次写入会覆盖之前的操作"""
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter(file_path)
    df.to_excel(excel_writer=writer, sheet_name=sheet_name, index=False)
    writer.save()
    writer.close()


def excel_add_sheet(data, file_path, sheet_name):
    """每次写入不会覆盖之前的操作，优先选用这个方法"""
    excel_writer = pd.ExcelWriter(file_path)
    book = load_workbook(excel_writer.path)
    excel_writer.book = book
    df = pd.DataFrame(data)
    df.to_excel(excel_writer=excel_writer, sheet_name=sheet_name, index=False)
    excel_writer.save()
    excel_writer.close()


if __name__ == '__main__':
    data = get_data(EXCEL_PATH, 'Sheet2')

    print(data['reback_command'].unique())
