#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 21:47
# @Author  : Yu xiang
# @File    : base_page.py

from scripts.log_class import loger
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from scripts.base_path import LOG_IMG_DIR
from datetime import datetime
from selenium import webdriver


class BasePage(object):

    def __init__(self, driver: Chrome):
        self.driver = driver

    def get_url(self):
        return self.driver.current_url

    def clear_input(self, locator):
        """clear input data"""
        return self.driver.find_element(*locator).clear()

    def wait_click_element(self, locator):
        """until could click element"""
        try:
            return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        except AttributeError as e:
            loger.error('元素不可点击定位出错')
            self.save_screen_shot()
            raise e

    def wait_visible_element(self, locator):
        """element can be saw wait 20 s"""
        try:
            return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        except AttributeError as e:
            loger.error('元素不可见定位出错')
            self.save_screen_shot()
            raise e

    def wait_presence_element(self, locator):
        """wait 20 s until element show"""
        try:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        except AttributeError as e:
            loger.error('定位元素出错')
            self.save_screen_shot()
            raise e

    def save_screen_shot(self):
        """take photos"""
        shot_name = LOG_IMG_DIR + '\\' + str(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")) + '.png'
        self.driver.save_screenshot(shot_name)
        print('ha')

    def operate_js(self, js):
        """执行js脚本"""
        return self.driver.execute_script(js)

    def double_click(self):
        pass

    def scroll(self):
        pass


if __name__ == "__main__":
    driver  = webdriver.Chrome()
    base_page = BasePage(driver)
    base_page.save_screen_shot()
