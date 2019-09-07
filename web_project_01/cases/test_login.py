#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-07 00:18
# @Author  : Xiang Yu
# @File    : bid_data.py
# @company : BEIJING-INTENGINE

import unittest
from ddt import ddt, data
from datas.login_data import pass_data, error_data, no_authority_data
from pages.login_page import LoginPage
from selenium import webdriver
from scripts.log_class import loger


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):  # 前置条件
        cls.driver = webdriver.Chrome()
        cls.login_page = LoginPage(cls.driver)
        cls.driver.implicitly_wait(5)
        # cls.driver.get(cls.login_page.url)

    @data(*pass_data)
    def test_01_pass(self, pass_data):  # 登录成功的测试用例
        url = self.login_page.pass_login(pass_data[0], pass_data[1])
        # url = self.login_page.current_url()
        try:
            self.assertEqual(url, pass_data[2])
            loger.info('账号为 {} 密码为 {} 的测试用例通过！'.format(pass_data[0], pass_data[1]))
        except AssertionError as e:
            loger.error('账号为 {} 密码为 {} 的测试用例不通过！'.format(pass_data[0], pass_data[1]))
            raise e

    @data(*error_data)  # 错误的账号或密码的测试用例
    def test_02_error(self, error_data):
        self.login_page.fail_login(error_data[0], error_data[1])
        error_msg = self.login_page.actual_result().text
        try:
            self.assertEqual(error_msg, error_data[2])
            loger.info('账号为 {} 密码为 {} 的测试用例通过！'.format(error_data[0], error_data[1]))
        except AssertionError as e:
            loger.error('账号为 {} 密码为 {} 的测试用例不通过！'.format(error_data[0], error_data[1]))
            raise e

    @data(*no_authority_data)  # 没有权限的登录的测试用例
    def test_03_no_auth(self, no_auth):
        self.login_page.fail_login(no_auth[0], no_auth[1])
        no_auth_msg = self.login_page.no_auth_result().text
        try:
            self.assertEqual(no_auth_msg, no_auth[2])
            loger.info('账号为 {} 密码为 {} 的测试用例通过！'.format(no_auth[0], no_auth[1]))
        except AssertionError as e:
            loger.error('账号为 {} 密码为 {} 的测试用例不通过！'.format(no_auth[0], no_auth[1]))
            raise e

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
