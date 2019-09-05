#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : test_login.py
import unittest
from ddt import ddt, data
from datas.login_data import pass_data, error_data
from pages.login_page import LoginPage
from selenium import webdriver


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.login_page = LoginPage(cls.driver)
        cls.driver.implicitly_wait(10)
        # cls.driver.get(cls.login_page.url)

    @data(*pass_data)
    def test_pass(self, pass_data):
        self.login_page.login(pass_data[0], pass_data[1])
        url = self.login_page.current_url()
        self.assertEqual(url, pass_data[2])
    # def test_error(self):
    #     pass

    @classmethod
    def tearDown(cls):
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()
