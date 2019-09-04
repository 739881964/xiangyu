import logging
from scripts.get_cfg import config
from scripts.base_path import LOGS_FILE_PATH


class Logger(object):

    def __init__(self):
        self.loger = logging.getLogger(config.get_value('log', 'loger_name'))  # 日志解释器对象
        self.loger.setLevel(config.get_value('log', 'loger_level'))  # 日志解释器日志等级

        # 日志输出方式
        console_log = logging.StreamHandler()  # 控制台输出
        file_log = logging.FileHandler(LOGS_FILE_PATH, encoding='utf-8')  # 文件输出

        # 日志输出格式
        simple_log = logging.Formatter(config.get_value('log', 'simple'))
        more_log = logging.Formatter(config.get_value('log', 'more'))

        console_log.setFormatter(simple_log)
        file_log.setFormatter(more_log)

        # 输出等级
        console_log.setLevel(config.get_value('log', 'console_level'))
        file_log.setLevel(config.get_value('log', 'file_level'))

        self.loger.addHandler(console_log)
        self.loger.addHandler(file_log)

    def get_log(self):
        return self.loger


loger = Logger().get_log()
