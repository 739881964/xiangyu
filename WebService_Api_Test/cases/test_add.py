# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 17:26
# @Author  : Xiang Yu
# @File    : test_add.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


from scripts.calc_math import Calc
from scripts.excel_class import ExcelClass
from scripts.get_cfg import config
from scripts.log_class import loger
from concurrent.futures.thread import ThreadPoolExecutor
from scripts.base_path import TEST_DATAS_EXCEL_PATH


class TestAdd(ExcelClass):

    def test_add(self, case):
        case_id = case['case_id']
        title = case['title']
        i_data = case['i_data']
        r_data = case['r_data']
        expected = case['expected']

        calc_res = Calc(i_data, r_data).add()
        msg = '测试' + title
        success_msg = config.get_value('res', 'success_res')
        fail_msg = config.get_value('res', 'fail_res')

        try:
            if expected == calc_res:
                loger.info('{} 的执行结果为: {}'.format(msg, success_msg))
                self.write_data_in_excel(case_id + 1, calc_res, success_msg)
            else:
                loger.error('{} 的执行结果为: {}'.format(msg, fail_msg))
                self.write_data_in_excel(case_id + 1, calc_res, fail_msg)
                print(msg, '不通过!')
        except:
            pass

    def run(self):
        data = self.read_excel_all_data()
        with ThreadPoolExecutor(max_workers=len(data)) as pool:
            for i in data:
                pool.map(self.test_add, [i])


if __name__ == "__main__":
    test = TestAdd(TEST_DATAS_EXCEL_PATH, '加法')
    test.run()

