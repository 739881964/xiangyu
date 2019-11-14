# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 16:55
# @Author  : Xiang Yu
# @File    : modify_c_file.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os
import chardet
import re


def modify_files(path):
    all_file = os.listdir(path)
    for file in all_file:
        one_dir_path = os.path.join(path, file)

        if (file.endswith('.cc')) or (file.endswith('.h')):
            f = open(one_dir_path, 'rb')
            data = f.read()
            file_encoding = chardet.detect(data).get('encoding')
            f.close()

            with open(one_dir_path, 'r', encoding=file_encoding) as f:
                data = f.readlines()
                # print(data)

                if data:
                    _data = list(map(lambda x: x.rstrip('\n'), data))
                    # print(_data)
                    new_path = os.path.join(path, f'8_{file}')
                    with open(new_path, 'a+', encoding='utf-8') as w:
                        for one_data in _data:
                            if one_data.startswith('#include'):
                                if '<' not in one_data:
                                    pattern = re.compile('"(.+\.h)"')
                                    if pattern.findall(one_data):
                                        find_data = pattern.findall(one_data)[0]
                                        if '/' in find_data:
                                            finally_data = one_data.replace(find_data, find_data.split('/')[-1])
                                            w.write(finally_data + '\n')
                                        else:
                                            w.write(one_data + '\n')
                                    else:
                                        w.write(one_data + '\n')
                                else:
                                    w.write(one_data + '\n')
                            else:
                                w.write(one_data + '\n')

            first_path = os.path.join(path, f'3_{file}')
            os.rename(one_dir_path, first_path)
            os.rename(new_path, one_dir_path)
            os.remove(first_path)

        elif os.path.isdir(one_dir_path):
            modify_files(one_dir_path)
        else:
            pass


if __name__ == "__main__":
    _path = r'C:\Users\xiangyu\Desktop\no_noise_word_list'
    modify_files(_path)

