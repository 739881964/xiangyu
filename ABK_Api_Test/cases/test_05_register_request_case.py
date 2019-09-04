import unittest
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.excel_class import ExcelClass
from libs.my_ddt import *
from scripts.get_cfg import config
from scripts.log_class import loger
from scripts.http_request_class import HttpRequest
from scripts.base_path import TEST_DATAS_EXCEL_PATH, REPORTS_PATH
# from scripts.params_replace import ParamsReplace
# from scripts.mysql_class import MysqlManual
from scripts.parsmas_replace_to_data import params_replace


excel = ExcelClass(TEST_DATAS_EXCEL_PATH, '注册')
case_name = excel.read_excel_all_data()


@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.http = HttpRequest()
        loger.info('------测试开始------')

    @data(*case_name)
    def test_register(self, case):
        case_id = case['case_id']
        title = case['title']
        method = case['method']
        expected = case['expected']

        url = config.get_value('start url', 'start_url') + case['url']
        params = params_replace(case['params'])

        actual_res = (self.http.get_method(method, url, data=params))['msg']

        msg = title + '的测试用例'
        success_msg = config.get_value('res', 'success_res')
        fail_msg = config.get_value('res', 'fail_res')

        try:
            self.assertEqual(expected, actual_res, msg=msg)
            loger.info('{} 的执行结果为: {}'.format(msg, success_msg))
            excel.write_data_in_excel(case_id+1, actual_res, success_msg)

        except AssertionError as e:
            print(msg, '不通过!')
            loger.error('{} 的执行结果为: {}, 失败的原因是: {}'.format(msg, fail_msg, actual_res))
            excel.write_data_in_excel(case_id+1, actual_res, fail_msg)
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http.close_session()
        loger.info('------测试结束------')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(TestRegister)
    suite.addTest(tests)
    with open(REPORTS_PATH+'/register.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='login test',
                                description='test_login',
                                tester='余翔'
                                )
        runner.run(suite)
