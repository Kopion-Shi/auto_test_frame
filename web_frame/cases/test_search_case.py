# -*- coding: utf-8 -*-
# @Time    : 2023/3/19 17:19
# @Author  : 石鑫磊
# @Site    : 
# @File    : test_search_case.py
# @Software: PyCharm 
# @Comment :
# ! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time

import pytest

sys.path.append('./../')
import os

from etc.config import BASEDIR
from tools.get_logger import MyLogger
from tools.get_data import Conf_info
from pages.index_page import IndexPage

LOGGER = MyLogger().get_logger_web_test()


class Test_case_search:

    """
    搜索功能测试用例

    """
    datas = Conf_info(file_read_path=os.path.join(BASEDIR, 'datas/search_datas.yaml')).get_data_from_yaml()


    def setup(self):
        print('setup')
        LOGGER.info('START TO EXECUTE TEST CASE')
        self.index = IndexPage()
        self.index._get_url('https://www.baidu.com/')

    def teardown(self):
        print('teardown')
        self.index._quit_driver()

    @pytest.mark.parametrize("text", datas)  # 数据参数化，实现数据驱动
    def test_search(self, text):
        # print(text)
        self.index.search_contact(text=text)
        time.sleep(3)
        print('------------',self.index._get_title())
        assert text[0] in self.index._get_title()  # 添加断言
        LOGGER.info('EXECUTE TEST CASE SUCCESS')


if __name__ == "__main__":
    pytest.main(["-vs", "test_search_case.py"])
