# coding=utf-8
import re
from scripts.log_manual import log


def read_list_txt(file_name):
    """
    获取txt内容为list
    """
    with open(file_name, 'r') as f:  # encoding='utf-8'
        lines = f.readlines()

    return lines


def read_str_txt(file_name):
    """
    获取txt内容为str
    """
    with open(file_name, 'r') as f:  # encoding='utf-8'
        lines = f.read()

    return lines


def read_log_file_str(file_name):
    """
    读取日志文件
    """
    with open(file_name, 'r') as f:
        text = f.read()

    return text


def read_log_to_list(file_name):
    """
    读取日志文件
    """
    with open(file_name, 'r') as f:
        text = f.readlines()

    return text


def read_rstrip_data(file_name):
    """去掉换行符号后的data列表"""
    data = []
    for line in open(file_name):
        res = line.rstrip('\n')
        data.append(res)

    return data


def write_txt_once(file_path, data):
    """
    写入内容到txt文件一次
    """
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(data + '\n')


def write_txt_one_more(file_path, data, int_num):
    """
    写入内容到txt文件多次
    """
    with open(file_path, 'a', encoding='utf-8') as f:
        for i in range(int_num):
            f.write(data + '\n')

def get_zh(str):
    """
    提取字符串中所有的中文，包括去重
    """
    des_res = []
    res = re.findall('[\u4e00-\u9fa5]+', str)
    for i in res:
        if i not in des_res:
            des_res.append(i)

    return des_res


def count_times(text, data):
    """
    计算单词出现的次数
    """
    for word in data:
        try:
            res = word + ' —→ 出现的次数是: ' + str(text.count(word)) + '次'
            log.info(res)
            print(res)
        except:
            res = f'要查询的单词 {word} 不存在'
            log.error(res)
