# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 10:19
# @Author  : Xiang Yu
# @File    : named_tuple.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import json
from collections import namedtuple  # 命名元组
from random import choice, shuffle


Card = namedtuple('Card', ['rank', 'suit'])  # 类似于类属性，无方法


class PlayDeck:

    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = ['红心', '方块', '黑桃', '梅花']

    def __init__(self):
        """ 设置牌数 """
        self._card = [Card(rank, suit) for rank in PlayDeck.ranks for suit in PlayDeck.suits]

    def __len__(self):
        """ 计算牌数 """
        return len(self._card)

    def __getitem__(self, item):
        """ 抽牌 """
        return self._card[item]

    def __setitem__(self, key, value):
        """ 洗牌要实现 __setitem__ 方法"""
        self._card[key] = value

    def __str__(self):
        return json.dumps(self._card, ensure_ascii=False)


deck = PlayDeck()
print(deck[0])
print(choice(deck))
shuffle(deck)
print(deck[0])
print(deck)
print(deck.ranks)

