# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 15:41
# @Author  : Xiang Yu
# @File    : download_photos.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os
import re
import requests

from urllib import request
from concurrent.futures.thread import ThreadPoolExecutor


class Spider:
    """ 获取图片 """
    url = 'http://desk.zol.com.cn/bizhi/5059_62711_2.html'
    save_path = r'C:\Users\xiangyu\Desktop\lol_heroes_photos'

    def get_html(self):
        """ 获取页面信息 """
        try:
            html = request.urlopen(self.url)
        except:
            print('获取所有图片时，由于网络问题，暂时无法连接到地址，请稍后重试......')
        else:
            html = html.read().decode('utf8', 'ignore')

            return html

    @staticmethod
    def get_photo_url(data):
        """ 提取图片url """
        if data:
            pattern = re.compile('src="(.+\.jpg)"')
            if pattern.findall(data):
                all_url = pattern.findall(data)

                return all_url
        else:
            print('传入图片的url为空')

    # @staticmethod
    # def get_whole_url(_url):
    #     """ 获取完整的url """
    #     all_url = list(map(lambda x: 'http:' + x, _url))
    #
    #     return all_url

    def download(self, i, urls, name):
        """ 下载图片到指定路径 """
        try:
            r = requests.get(urls[i])
        except:
            print('获取图片时，由于网络问题，暂时无法下载，请稍后重试......')
        else:
            one_name = f'{name}_{i}.jpg'
            path = os.path.join(self.save_path, one_name)
            with open(path, 'wb') as f:
                f.write(r.content)
                print('{}图片下载完成'.format(one_name))

    def main(self, data, name):
        """ 多线程(线程池)下载图片 """
        if data:
            with ThreadPoolExecutor(max_workers=100) as pool:
                for i in range(len(data)):
                    pool.map(self.download, [i], [data], [name])
        else:
            print('线程池失败')

    def go(self, name='周杰伦'):
        """ 所有函数的入口 """
        res = self.get_html()
        _data = self.get_photo_url(res)
        # whole_data = self.get_whole_url(_data)
        self.main(_data, name)


spider = Spider()
spider.go()

