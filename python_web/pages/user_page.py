#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/8/29 20:32
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserPage(BasePage):
    balance_locator = (By.CSS_SELECTOR, ".color_sub")

    @property
    def balance_element(self):
        return self.wait_visible_element(self.balance_locator)

    def get_balance(self):
        return self.balance_element.text[:-1]
