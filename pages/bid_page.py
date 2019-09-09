# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : 余翔
# @File    : test_login.py

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement



class BidPage(BasePage):

    bid_input_locator = (By.CLASS_NAME, 'form-control invest-unit-investinput')
    bid_button_locator = (By.CLASS_NAME, 'btn btn-special')
    pass_msg_locator = (By.XPATH, '//div[@class="layui-layer-content"]//div[@class="capital_font1 note"]')
    active_button_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")

    @property
    def bid_input(self) -> WebElement:
        """投资金额输入框"""
        return self.wait_visible_element(self.bid_input_locator)

    @property
    def bid_button(self) -> WebElement:
        """投资按钮"""
        return self.driver.find_element(*self.bid_button_locator)

    def pass_msg_element(self):
        return self.wait_visible_element(self.pass_msg_locator)

    def click_active_element(self):
        return self.wait_click_element(self.active_button_locator)

    def bid(self, money):
        """success bid steps"""
        e = self.bid_input
        balance = e.get_attribute('data_amount')
        e.send_keys(money)
        self.bid_button.click()
        return balance
