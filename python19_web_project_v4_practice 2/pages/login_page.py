#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/8/20 22:00

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class LoginPage(BasePage):
    # 共享数据的一种形式
    login_url = 'http://120.78.128.25:8765/Index/login.html'
    # 页面元素定位表达式,当需求发生变化，改的地方尽量的少，好找：可维护性强
    error_msg_locator = (By.CSS_SELECTOR, 'div.form-error-info')
    confirm_login_locator = (By.CSS_SELECTOR, 'button.btn-special')
    mobile_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    invalidate_msg_locator = (By.CSS_SELECTOR, '.layui-layer-content')

    def get_actual_result(self):
        """获取实际结果"""
        return self.driver.find_element(*self.error_msg_locator)

    @property
    def user_elem(self) -> WebElement:
        """定位用户"""
        return self.wait_presence_element(self.mobile_locator)

    @property
    def pwd_elem(self) -> WebElement:
        """定位密码"""
        return self.wait_presence_element(self.pwd_locator)

    def get_invalidate_result(self):
        """获取没有通过授权，必须等待"""
        return self.wait_visible_element(self.invalidate_msg_locator)

    def login(self, username, password):
        """登录"""
        self.driver.get(self.login_url)
        self.user_elem.send_keys(username)
        self.pwd_elem.send_keys(password)
        e = self.wait_click_element(self.confirm_login_locator)
        e.click()
