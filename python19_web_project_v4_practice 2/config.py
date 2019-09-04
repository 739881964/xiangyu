#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/8/27 21:35

import os
# from pathlib import Path
# path = Path(__file__)
# path.

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

LOG_IMG = os.path.join(ROOT_PATH, 'log_img')

# pathlib 标准库，os.path
if os.path.exists(LOG_IMG):
    pass
else:
    os.mkdir(LOG_IMG)
