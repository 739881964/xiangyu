# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm
import unittest
from scripts.calc_math import Calc
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.excel_class import ExcelClass
from libs.my_ddt import *
from scripts.get_cfg import config
from scripts.log_class import loger
from scripts.base_path import TEST_DATAS_EXCEL_PATH, REPORTS_PATH


excel = ExcelClass(TEST_DATAS_EXCEL_PATH, '减法')
case_name = excel.read_excel_all_data()


@ddt
class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        loger.info('------测试开始------')

    @data(*case_name)
    def test_add(self, case):
        case_id = case['case_id']
        title = case['title']
        i_data = case['i_data']
        r_data = case['r_data']
        expected = case['expected']

        calc_res = Calc(i_data, r_data).sub()
        msg = '测试' + title
        success_msg = config.get_value('res', 'success_res')
        fail_msg = config.get_value('res', 'fail_res')

        try:
            self.assertEqual(expected, calc_res, msg=msg)
            loger.info('{} 的执行结果为: {}'.format(msg, success_msg))
            excel.write_data_in_excel(case_id+1, calc_res, success_msg)
        except AssertionError as e:
            print(msg, '不通过!')
            loger.error('{} 的执行结果为: {}'.format(msg, fail_msg))
            excel.write_data_in_excel(case_id+1, calc_res, fail_msg)
            raise e

    @classmethod
    def tearDownClass(cls):
        loger.info('------测试结束------')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(TestAdd)
    suite.addTest(tests)
    with open(REPORTS_PATH+'\\sub.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='add test',
                                description='add_test_case_test',
                                tester='余翔'
                                )
        runner.run(suite)
