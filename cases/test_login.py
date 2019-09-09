#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : test_login.py

import unittest
from ddt import ddt, data
from datas.login_data import pass_data, error_data, no_authority_data
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

    @data(*pass_data)
    def test_pass(self, pass_data):
        """pass login"""
        url = self.login_page.login_pass(pass_data[0], pass_data[1])
        try:
            self.assertEqual(url, pass_data[2])
            loger.info('用户名：{}；密码：{} 测试用例执行成功！'.format(pass_data[0], pass_data[1]))
        except AssertionError as e:
            loger.error('用户名：{}；密码：{} 测试用例执行失败！'.format(pass_data[0], pass_data[1]))
            raise e

    @data(*no_authority_data)
    def test_error(self, no_data):
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
