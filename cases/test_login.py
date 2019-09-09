#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : test_login.py

import unittest
from ddt import ddt, data
from datas.login_data import login_pass_data, login_error_data, login_no_authority_data
from pages.login_page import LoginPage
from selenium import webdriver
from scripts.log_class import loger


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.login_page = LoginPage(cls.driver)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    # @data(*login_pass_data)
    def test_01_pass(self):
        """pass login"""
        url = self.login_page.login_pass(login_pass_data[0], login_pass_data[1])
        try:
            self.assertEqual(url, login_pass_data[2])
            loger.info('用户名：{}；密码：{} 测试用例执行成功！'.format(login_pass_data[0], login_pass_data[1]))
        except AssertionError as e:
            loger.error('用户名：{}；密码：{} 测试用例执行失败！'.format(login_pass_data[0], login_pass_data[1]))
            raise e

    @data(*login_no_authority_data)
    def test_02_error(self, no_data):
        """error login"""
        self.login_page.login_error(no_data[0], no_data[1])
        msg = self.login_page.get_no_auth_msg().text
        try:
            self.assertEqual(msg, no_data[2])
            loger.info('用户名：{}；密码：{} 测试用例执行成功！'.format(no_data[0], no_data[1]))
        except AssertionError as e:
            loger.error('用户名：{}；密码：{} 测试用例执行失败！'.format(no_data[0], no_data[1]))
            raise e

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
