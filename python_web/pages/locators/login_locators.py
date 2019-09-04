#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/8/24 11:27

from selenium.webdriver.common.by import By


# Keys .txt
class LoginLocator:
    error_msg_locator = (By.CSS_SELECTOR, 'div.form-error-info')
    confirm_login_locator = (By.CSS_SELECTOR, 'button.btn-special')
    mobile_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    invalidate_msg_locator = (By.CSS_SELECTOR, '.layui-layer-content')