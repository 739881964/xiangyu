# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : 余翔
# @File    : test_login.py

from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    home_url = 'http://120.78.128.25:8765/Index/index'
    home_bid_button_locator = (By.CSS_SELECTOR, '.btn-special')
    user_info_locator = (By.XPATH, '//a[@href="/Member/index.html"]')

    @property
    def home_bid_button_element(self) -> WebElement:
        """主页投资按钮"""
        return self.wait_click_element(self.home_bid_button_locator)

    def get_home_element(self):
        """主页url"""
        return self.driver.get(self.home_url)

    def user_info_element(self):
        """用户名称"""
        return self.wait_presence_element(self.user_info_locator)

    def click_bid(self):
        e = self.home_bid_button_element
        print(e.text)
        return e.click()
