#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/8/27 21:26
import logging
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome, ActionChains
import config


class BasePage:

    def __init__(self, driver:Chrome):
        self.driver = driver

    def wait_presence_element(self, locator):
        """等待元素出现"""
        try:
            return WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(locator))
        except Exception as e:
            logging.error('定位出错')
            self.save_screenshot()

    def wait_visible_element(self, locator):
        """等待元素可见"""
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    def wait_click_element(self, locator):
        """返回一个 WebElement 对象。如果没有找到，就报错。"""
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))

    def gen_screen_file_name_by_ts(self):
        """生成文件名通过现在的时间戳."""
        ts = str(int(time.time()))
        return ''.join((ts, '.png'))

    def save_screenshot(self):
        """自动化保存截图。"""
        # 文件路径。配置文件去保存。ini, yaml, py
        img_path = config.LOG_IMG
        file_name = os.path.join(img_path, self.gen_screen_file_name_by_ts())
        self.driver.save_screenshot(file_name)

    # 封装
    def get_url(self):
        return self.driver.current_url

    def switch_window(self, window_name):
        pass

    def switch_iframe(self, frame_reference):
        pass

    def switch_alert(self):
        pass

    # 鼠标操作
    # 滚动窗口
    # 键盘操作
    # webelement

    def double_click(self, elem):
        """双击"""
        action_chains = ActionChains(self.driver)
        return action_chains.double_click(elem).perform()

    def context_click(self, elem):
        """右击"""
        action_chains = ActionChains(self.driver)
        return action_chains.context_click(elem).perform()

    def scroll_window(self, width, height):
        """滚动到对应的窗口位置"""
        # webelement,scroll_into_view
        # js
        return self.driver.execute_script("window.scrollTo({}, {})".format(width, height))

    # 上传文件，
    def upload_file(self, elem, file_path):
        # 判断，input, elem.send_keys()
        # pywin32
        pass
