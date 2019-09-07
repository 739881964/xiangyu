#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-07 00:18
# @Author  : Xiang Yu
# @File    : bid_data.py
# @company : BEIJING-INTENGINE

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep


class LoginPage(BasePage):

    url = 'http://120.78.128.25:8765/Index/login.html'
    username_locator = (By.NAME, 'phone')
    password_locator = (By.NAME, 'password')
    login_button_locator = (By.CLASS_NAME, 'btn.btn-special')
    error_msg_locator = (By.CLASS_NAME, 'form-error-info')
    no_auth_locator = (By.CSS_SELECTOR, '.layui-layer-content')

    @property
    def username_element(self) -> WebElement:
        """username"""
        return self.wait_presence_element(self.username_locator)

    @property
    def password_element(self) -> WebElement:
        """password"""
        return self.wait_presence_element(self.password_locator)

    @property
    def login_button(self) -> WebElement:
        """login button"""
        return self.wait_click_element(self.login_button_locator)

    def actual_result(self):
        """actual result"""
        return self.driver.find_element(*self.error_msg_locator)

    def no_auth_result(self):
        """没有权限结果"""
        return self.driver.find_element(*self.no_auth_locator)

    def current_url(self):
        return self.driver.current_url

    def clear_username_and_password(self):
        self.username_element.clear()
        self.password_element.clear()

    def pass_login(self, username, password):
        """login steps"""
        self.driver.get(self.url)
        self.clear_username_and_password()
        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        e = self.wait_click_element(self.login_button_locator)
        e.click()
        sleep(1)
        return self.current_url()

    def fail_login(self, username, password):
        """失败登录"""
        self.driver.get(self.url)
        self.clear_username_and_password()
        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        self.wait_click_element(self.login_button_locator).click()
