#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/8/27 20:14


import time
import unittest
from decimal import Decimal
import pytest
from ddt import ddt, data
from selenium import webdriver
from data.bid_data import bid_error_data, bid_success_data
from data.login_data import user_info_error, user_info_invalidate, user_info_success
from pages.bid_page import BidPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.user_page import UserPage


@ddt
class TestBid(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.login_page = LoginPage(self.driver)
        self.login_page.login(user_info_success[0], user_info_success[1])
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


    @data(*bid_error_data)
    def test_bid_error(self, error_data):
        # 元素定位：.btn-special，
        home_page = HomePage(self.driver)
        # get
        home_page.get()
        home_page.click_bid_button()
        #
        bid_page = BidPage(self.driver)
        bid_page.bid_input.send_keys(error_data[0])
        self.assertEqual(bid_page.bid_confirm_button.text, error_data[1])

    @data(*bid_success_data)
    def test_bid_success(self, success_data):
        home_page = HomePage(self.driver)
        home_page.get()
        home_page.click_bid_button()
        bid_page = BidPage(self.driver)
        # bid_page.bid_input.send_keys(success_data[0])
        # bid_page.bid_confirm_button.click()
        balance = bid_page.bid_success(bid_success_data[0])
        # 111.11
        self.assertEqual(bid_page.bid_popup_msg.text, success_data[1])
        # 验证余额
        bid_page.click_bid_active_button()
        # 11.11
        actual_balace = UserPage(self.driver).get_balance()
        self.assertTrue(Decimal(balance) - Decimal(str(100)) == Decimal(actual_balace))
        # 测试计划：那些，优先级。
        # 接口更加通用。web
        # app 自动化


if __name__ == '__main__':
    unittest.main()
