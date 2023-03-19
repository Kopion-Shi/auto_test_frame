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
import allure
LOGGER = MyLogger().get_logger_web_test()


class Test_case_search:
    """
    搜索功能测试用例
    """
    datas = Conf_info(file_read_path=os.path.join(BASEDIR, 'datas/search_datas.yaml')).get_data_from_yaml()
    def setup(self):
        LOGGER.info('START TO EXECUTE TEST CASE')
        self.index = IndexPage()
        self.index._get_url('https://www.baidu.com/')


    def teardown(self):
        self.index._quit_driver()

    @pytest.mark.parametrize("text",datas) # 数据参数化，实现数据驱动
    def test_search(self,text):
        try:
            self.index.search_contact(text=text)
            time.sleep(3)
            assert text[0] in self.index._get_title() # 添加断言
            LOGGER.info('EXECUTE TEST CASE SUCCESS')
        except Exception as e:
            LOGGER.error(f'EXECUTE TEST CASE failed, the reason is {e}')
            img_path = os.path.join(BASEDIR,f'report/images/{get_now_time()}.png')
            self.index._get_screenshot_as_file(img_path) # 失败截图
            allure.attach.file(source=img_path,name='失败截图',attachment_type=allure.attachment_type.PNG) # 将失败截图上传到测试报告中
            raise e

if __name__ == "__main__":
    json_path = os.path.join(BASEDIR, f'reports/allure_result/{get_now_time()}')  # 指定生成的json报告文件的路径
    html_path = os.path.join(BASEDIR, f'reports/allure_report/{get_now_time()}')  # 指定生成的html报告文件的路径

    pytest.main(['-vs', 'test_search_case_allure.py', f'--alluredir={json_path}']) # 生成json报告
    os.system(f'allure generate {json_path} -o {html_path}') # 使用allure生成HTML报告
