# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 10:24
# @Author  : Xiang Yu
# @File    : md5.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import hashlib


class UserLogin:

    def __init__(self, path):
        self.path = path

    @staticmethod
    def md5(string, salt=None):
        """ MD5加盐 """
        if salt:
            hs = hashlib.md5(salt.encode('utf-8'))  # cedfcd04d30a113e5f3ba92201bad0b9
        else:
            hs = hashlib.md5()
        hs.update(string.encode('utf-8'))  # 449254a968d87896920ea8f7e5719879
        pwd = hs.hexdigest()

        return pwd

    def user_login(self):
        """ 用户输入账号和密码 """
        with open(self.path) as f:
            pd = list(map(lambda x: x.rstrip('\n'), f.readlines()))
        error_times = 0
        while True:
            username = input('请输入姓名：')
            password = self.md5(input('请输入密码：'), '941124')
            # print(password)
            if username == pd[0] and password == pd[1]:
                print('login success ！')
                break
            else:
                print('username or password error ...')
                error_times += 1
                if error_times >= 4:
                    print('请输入的次数过多，五分钟后再尝试......')
                    break


if __name__ == "__main__":
    _path = r'C:\Users\xiangyu\xiangyu_git\work_directory\projects\save_screct'
    login = UserLogin(_path)
    login.user_login()

