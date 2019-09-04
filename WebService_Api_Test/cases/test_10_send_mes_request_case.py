# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm


import unittest
# from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.excel_class import ExcelClass
from libs.my_ddt import *
from scripts.get_cfg import config
from scripts.log_class import loger
from scripts.base_path import TEST_DATAS_EXCEL_PATH, REPORTS_PATH
from scripts.webservice_request_class import WebServiceRequest
# from suds.sudsobject import asdict
# import suds
from scripts.webservice_parsmas_replace_to_data import params_replace


excel = ExcelClass(TEST_DATAS_EXCEL_PATH, 'send_message')
case_name = excel.read_excel_all_data()


@ddt
class TestSendMessage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        loger.info('------TestStart------')

    @data(*case_name)
    def test_send_message(self, case):
        case_id = case['case_id']
        title = case['title']
        expected = case['expected']
        url = case['url']
        method = case['method']

        msg = '测试用例为：' + title
        success_msg = config.get_value('res', 'success_res')
        fail_msg = config.get_value('res', 'fail_res')

        new_params = params_replace(case['params'])
        res = WebServiceRequest.to_data(url, method, new_params)  # str类型

        try:
            self.assertEqual(expected, res, msg=msg)
            loger.info('{} 执行结果是: {}'.format(msg, success_msg))
            excel.write_data_in_excel(case_id+1, res, success_msg)

        except AssertionError as e:
            loger.error('{} 执行结果是: {}, 失败的原因是: {}'.format(msg, fail_msg, e))
            excel.write_data_in_excel(case_id+1, e, fail_msg)
            raise e

    @classmethod
    def tearDownClass(cls):
        loger.info('-------TestEnd-------')


if __name__ == '__main__':
    unittest.main()
