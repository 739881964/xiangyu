# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : 余翔
# @File    : test_login.py

import unittest
from pages.user_page import UserPage
from pages.bid_page import BidPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from ddt import ddt, data
from selenium import webdriver
from scripts.log_class import loger
from datas.bid_data import bid_pass_data, bid_error_data
from datas.login_data import login_pass_data
from decimal import Decimal


@ddt
class TestBid(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.login_page = LoginPage(cls.driver)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.login_page.login_pass(login_pass_data[0], login_pass_data[1])

    @data(*bid_pass_data)
    def test_01_success_bid(self, pass_data):
        home_page = HomePage(self.driver)
        home_page.get_url()
        home_page.click_bid()
        bid_page = BidPage(self.driver)
        balance = bid_page.bid(pass_data[0])
        try:
            self.assertEqual(bid_page.pass_msg_element(), pass_data[1])
            loger.info('投资金额为：{} 的测试用例执行成功！'.format(pass_data[0]))
        except AssertionError as e:
            loger.error('投资金额为：{} 的测试用例执行失败！'.format(pass_data[0]))
            raise e
        bid_page.click_active_element()
        after_balance = UserPage(self.driver).get_money()
        try:
            self.assertTrue(Decimal(balance) - Decimal(str(bid_pass_data[0] == Decimal(after_balance))))
            loger.info('投资金额为：{} 的测试用例执行成功！'.format(pass_data[0]))
        except AssertionError as e:
            loger.error('投资金额为：{} 的测试用例执行失败！'.format(pass_data[0]))
            raise e

    @data(*bid_error_data)
    def test_02_error_bid(self, error_data):
        home_page = HomePage(self.driver)
        home_page.get_url()
        home_page.click_bid()
        bid_page = BidPage(self.driver)
        bid_page.bid_input.send_keys(error_data[0])
        try:
            self.assertEqual(bid_page.bid_button.text, error_data[1])
            loger.info('投资金额为：{} 的测试用例执行成功！'.format(error_data[0]))
        except AssertionError as e:
            loger.error('投资金额为：{} 的测试用例执行失败！'.format(error_data[0]))
            raise e

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
