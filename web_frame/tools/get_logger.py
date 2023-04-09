# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2023/3/18 10:01
# @Author  : 石鑫磊
# @Site    : 
# @File    : get_logger.py
# @Software: PyCharm 
# @Comment :
import logging  # 导入logging模块
import logging.config
import os
##解决window平台的编解码问题
import _locale
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])


class MyLogger:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config/logging.conf')

    def get_logger_root(self, confName="root"):
        logging.config.fileConfig(self.config_path)
        logger = logging.getLogger(confName)
        return logger

    def get_logger_web_test(self, confName="webtest"):
        logging.config.fileConfig(self.config_path)
        logger = logging.getLogger(confName)
        return logger

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.shutdown()


if __name__ == "__main__":
    # 生成一个logger实例
    web_log = MyLogger().get_logger_web_test()
    web_log.info('success')  # 使用logger来输出日志
    web_log.error('failed')
