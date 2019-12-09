# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 10:44
# @Author  : Xiang Yu
# @File    : upgrade_app.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import time
import numpy as np
from projects.receive_send_serial import OperationSerial


class UpGrade(OperationSerial):
    """ 升级版本 """

    def write_data(self):
        if self.is_open():
            self.port.write('VOI611\n'.encode('utf8'))
            time.sleep(0.5)
        if not self.is_open():
            self.port.write(' '.encode('utf8'))



if __name__ == "__main__":
    UpGrade('COM4').write_data()
