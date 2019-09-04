#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/8/22 21:23

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    home_url = 'http://120.78.128.25:8765'
    bid_locator  =  (By.CSS_SELECTOR, '.btn-special')
    user_locator = (By.XPATH, "//a[@href='/Member/index.html']")

    def get(self):
        return self.driver.get(self.home_url)

    @property
    def user_element(self):
        """用户昵称"""
        return self.wait_presence_element(self.user_locator)

    @property
    def bid_button(self):
        """首页投标按钮"""
        return self.wait_click_element(self.bid_locator)

    def click_bid_button(self):
        """点击首页投标"""
        e = self.bid_button
        print(e.text)
        return e.click()
