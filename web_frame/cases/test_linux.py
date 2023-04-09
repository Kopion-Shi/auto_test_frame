# -*- coding: utf-8 -*-
# @Time    : 2023/3/19 19:06
# @Author  : 石鑫磊
# @Site    : 
# @File    : test_search_case_allure.py
# @Software: PyCharm 
# @Comment :
#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time

import pytest

sys.path.append('./../')
import os

from etc.config import BASEDIR
from tools.get_logger import MyLogger
from tools.get_data import Conf_info
from tools.get_strtime import get_now_time
from pages.index_page import IndexPage
from tools.ssh_tools import SSHProxy
import allure
LOGGER = MyLogger().get_logger_web_test()


class Test_case_search:
    """
    搜索功能测试用例
    """
    datas = Conf_info(file_read_path=os.path.join(BASEDIR, 'datas/linux_datas.yaml')).get_data_from_yaml()
    def setup(self):
        print('setup')
        self.ssh=SSHProxy()

    def teardown(self):
        # self.ssh.cloes()
        print('teardown')

    @pytest.mark.parametrize("cmd_set",datas) # 数据参数化，实现数据驱动
    def test_cmd(self,cmd_set):
        for i in range(50000):
            for cmd_ in cmd_set:
                # print('第{}次查询'.format(i))
                LOGGER.info('第{}次查询'.format(i))
                res=self.ssh.command(cmd_)
                self.ssh.download(os.path.join(BASEDIR, 'source/saba_set.sh'),'/root/saba_set.sh')
                print(res)

if __name__ == "__main__":
    # json_path = os.path.join(BASEDIR, f'reports/allure_result/{get_now_time()}')  # 指定生成的json报告文件的路径
    # html_path = os.path.join(BASEDIR, f'reports/allure_report/{get_now_time()}')  # 指定生成的html报告文件的路径

    pytest.main(['-vs', '-n 4',r'D:\00_github\autotest_frame\web_frame\cases\test_linux.py']) # 生成json报告
    # pytest.main(['-vs', '-n 4','test_search_case_allure.py', f'--alluredir={json_path}']) # 生成json报告
    # os.system(f'allure generate {json_path} -o {html_path}') # 使用allure生成HTML报告
