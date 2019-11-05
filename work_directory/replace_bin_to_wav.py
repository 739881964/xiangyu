# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 17:20
# @Author  : Xiang Yu
# @File    : replace_bin_to_wav.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import os
from path.test_path import Info
from scripts.text_manual import get_all_file
from scripts.pandas_manual import PandasManual


# rename bin to wav or pcm
to_csv = PandasManual(r'C:\Users\xiangyu\Desktop\work_dir\datas\excel.csv')
data = to_csv.read_csv()

name = data['wav_name'].tolist()
wav_name_list = list(map(lambda x: x.split('\\')[-1], name))

all_bin_name = get_all_file(Info.bin_path)
pass
for i in range(len(name)):
    one_name = os.rename(os.path.join(Info.bin_path, all_bin_name[i]),
                         os.path.join(Info.bin_path,  wav_name_list[i]))
    print(one_name)

