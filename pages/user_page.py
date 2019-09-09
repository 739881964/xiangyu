# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : 余翔
# @File    : test_login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from pages.base_page import BasePage



class UserPage(BasePage):

    user_visible_money_locator = (By.CLASS_NAME, 'color_sub')

    @property
    def user_visible_element(self) -> WebElement:
        """可用余额"""
        return self.wait_visible_element(self.user_visible_money_locator)

    def get_money(self):
        e = self.user_visible_element.text[:-1]
        return e
