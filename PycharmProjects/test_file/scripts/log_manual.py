import logging
from scripts.conf_manual import config
from scripts.base_path import LOG_FILE_PATH


class LogManual(object):

    def __init__(self):
        # 定义日志对象log的名称name和日志等级lv
        self.log = logging.getLogger(config.get_value('log', 'log_name'))
        self.log.setLevel(config.get_value('log', 'log_lv'))

        # 添加日志输出形式，文件与控制台
        file_log = logging.FileHandler(LOG_FILE_PATH)
        console_log = logging.StreamHandler()

        # 添加形式输出的日志等级
        file_log.setLevel(config.get_value('log', 'file_lv'))
        console_log.setLevel(config.get_value('log', 'console_lv'))

        # log输出格式
        more_log = logging.Formatter(config.get_value('log', 'more'))
        simple_log = logging.Formatter(config.get_value('log', 'simple'))

        # 绑定输入格式
        file_log.setFormatter(more_log)
        console_log.setFormatter(simple_log)

        self.log.addHandler(file_log)
        self.log.addHandler(console_log)

    def get_log(self):
        return self.log


log = LogManual().get_log()


if __name__ == '__main__':
    log.info('this is a info log')
    log.error('this is a error log')
