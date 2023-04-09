# -*- coding: utf-8 -*-
# @Time    : 2023/3/21 22:04
# @Author  : 石鑫磊
# @Site    : 
# @File    : run.py
# @Software: PyCharm 
# @Comment :
import sys
import time

import pytest

sys.path.append('/')
import os

from etc.config import BASEDIR
from tools.get_logger import MyLogger
from tools.get_data import Conf_info
from tools.get_strtime import get_now_time
from pages.index_page import IndexPage
import allure

LOGGER = MyLogger().get_logger_web_test()

if __name__ == "__main__":
    # json_path = os.path.join(BASEDIR, f'reports/allure_result/{get_now_time()}')  # 指定生成的json报告文件的路径
    # html_path = os.path.join(BASEDIR, f'reports/allure_report/{get_now_time()}')  # 指定生成的html报告文件的路径

    # pytest.main(['-vs', '-n 4','test_search_case_allure.py', f'--alluredir={json_path}']) # 生成json报告
    # case_path=os.path.join(BASEDIR,'/cases/test_search_case_allure.py')
    # case_path = os.path.join(BASEDIR, '/cases/test_linux.py')
    # print(case_path)
    cpu_num=os.cpu_count()

    pytest.main(['-vs', '-n {}'.format(cpu_num),r'D:\00_github\autotest_frame\web_frame\cases\test_linux.py'])
    # pytest.main(['-vs', '-n 4','/opt/project/web_frame/cases/test_linux.py']) # 生成json报告
    # pytest.main(['-vs', '-n {}'.format(cpu_num),r'D:\00_github\autotest_frame\web_frame\cases\test_search_case_allure.py']) # 生成json报告
    # os.system(f'allure generate {json_path} -o {html_path}') #
