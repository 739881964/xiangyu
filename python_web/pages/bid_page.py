#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/8/27 20:32
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BidPage(BasePage):
    bid_input_locator = (By.CSS_SELECTOR, '.form-control')
    bid_confirm_locator = (By.CSS_SELECTOR, '.btn-special')
    bid_popup_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='capital_font1 note']")
    bid_active_button_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")


    @property
    def bid_input(self):
        """投资输入框"""
        return self.wait_visible_element(self.bid_input_locator)

    def bid_success(self, money):
        """投资成功"""
        e = self.bid_input
        balance = e.get_attribute('data-amount')
        e.send_keys(money)
        self.bid_confirm_button.click()
        return balance

    @property
    def bid_confirm_button(self):
        """投资确认按钮"""
        return self.wait_visible_element(self.bid_confirm_locator)

    @property
    def bid_popup_msg(self):
        """找到投标成功的元素"""
        return self.wait_visible_element(self.bid_popup_msg_locator)

    def click_bid_active_button(self):
        return self.wait_click_element(self.bid_active_button_locator).click()
