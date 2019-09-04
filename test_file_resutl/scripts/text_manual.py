import re
from scripts.log_manual import log


def read_list_txt(file_name):
    """get txt content to list"""
    with open(file_name, 'r', encoding='gbk') as f:  # encoding='utf-8'
        lines = f.readlines()
    return lines


def read_str_txt(file_name):
    """get txt content to str"""
    with open(file_name, 'r', encoding='gbk') as f:  # encoding='utf-8'
        lines = f.read()
    return lines


def read_log_file_str(file_name):
    """read log file"""
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def read_log_to_list(file_name):
    """read log file"""
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.readlines()
    return text


def read_rstrip_data(file_name):
    """abandon \n from data to list"""
    data = []
    for line in open(file_name, encoding='gbk'):
        res = line.rstrip('\n')
        data.append(res)
    return data


def write_txt_once(file_path, data):
    """write to txt once """
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(data + '\n')


def write_txt_one_more(file_path, data, int_num):
    """write content to txt more times"""
    with open(file_path, 'a', encoding='utf-8') as f:
        for i in range(int_num):
            f.write(data + '\n')


def get_zh(str):
    """get Chinese from str and duplicate removal"""
    des_res = []
    res = re.findall('[\u4e00-\u9fa5]+', str)
    for i in res:
        if i not in des_res:
            des_res.append(i)
    return des_res


def get_one_key(str):
    """get Chinese"""
    res = re.findall('[\u4e00-\u9fa5]+', str)[0]
    return res


def count_times(text, data):
    """circulate word appear times"""
    for word in data:
        try:
            res = word + ' —→ appear times is : ' + str(text.count(word)) + '次'
            log.info(res)
            print(res)
        except:
            res = f'Search word: {word} not exist'
            log.error(res)
