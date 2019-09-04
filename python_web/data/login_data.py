#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/8/24 9:52


user_info_success = ('18684720553', 'python', 's')


user_info_error = [
    ('', '', '请输入手机号'),
    ('12', '', '请输入正确的手机号'),
    ('15679876534', '', '请输入密码')
]

# TODO: 数据分组的依据是什么？？操作步骤是否一致，定位表达式是否一致
# user_info_invalidate 没有授权
# 测试数据分组
user_info_invalidate = [
    ('15679876534', '12', '此账号没有经过授权'),
    ('18684720553', '12', '帐号或密码错误!')
]
