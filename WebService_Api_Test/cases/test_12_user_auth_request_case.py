# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm


import json
import unittest
# from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.excel_class import ExcelClass
from libs.my_ddt import ddt, data
from scripts.get_cfg import config
from scripts.log_class import loger
from scripts.base_path import TEST_DATAS_EXCEL_PATH, REPORTS_PATH
from scripts.webservice_parsmas_replace_to_data import params_replace, ParamsReplaces
from scripts.webservice_request_class import WebServiceRequest
# from suds.client import Client
# from suds import sudsobject
from scripts.mysql_class import MysqlManual


excel = ExcelClass(TEST_DATAS_EXCEL_PATH, 'user_auth')
case_name = excel.read_excel_all_data()


@ddt
class TestUserAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mysql = MysqlManual()
        loger.info('------测试开始------')

    @data(*case_name)
    def test_user_auth(self, case):
        case_id = case['case_id']
        title = case['title']
        expected = case['expected']

        msg = title + '的测试用例'
        success_msg = config.get_value('res', 'success_res')
        fail_msg = config.get_value('res', 'fail_res')

        url = case['url']
        method = case['method']
        new_params = params_replace(case['params'])
        actual_res = WebServiceRequest.to_data(url, method, new_params)

        if 'ok' in actual_res:
            check_sql = case["check_sql"]
            if check_sql:
                if '#sql_mobile#' in check_sql:
                    sql_one_mobile = json.loads(new_params)
                    setattr(ParamsReplaces, 'sql_mobile', sql_one_mobile['mobile'])
                    setattr(ParamsReplaces, 'end_two_num', sql_one_mobile['mobile'][-2:])
                    setattr(ParamsReplaces, 'third_num', sql_one_mobile['mobile'][-3:-2])
                    check_sql = params_replace(check_sql)
                    res_dict = self.mysql.run_sql(check_sql)
                    setattr(ParamsReplaces, 'mes_code', res_dict['Fverify_code'])
                else:
                    exit_random_name = json.loads(new_params)
                    setattr(ParamsReplaces, 'exit_name', exit_random_name['user_id'])
                    check_sql = params_replace(check_sql)
                    res_dict = self.mysql.run_sql(check_sql)
                    setattr(ParamsReplaces, 'uid', str(res_dict['Fuid']))
                    # print(type(res_dict['Fuid']))

        try:
            self.assertIn(expected, actual_res, msg=msg)
            loger.info('{} 的执行结果为: {}'.format(msg, success_msg))
            excel.write_data_in_excel(case_id+1, actual_res, success_msg)
        except AssertionError as e:
            print(msg, '不通过!')
            loger.error('{} 的执行结果为: {}, 失败的原因是: {}'.format(msg, fail_msg, actual_res))
            excel.write_data_in_excel(case_id+1, actual_res, fail_msg)
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close_db()
        loger.info('------测试结束------')


if __name__ == '__main__':
    unittest.main()
