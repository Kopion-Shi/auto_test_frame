# -*- coding: utf-8 -*-
# @Time    : 2023/3/19 10:02
# @Author  : 石鑫磊
# @Site    : 
# @File    : index_page.py
# @Software: PyCharm 
# @Comment :
#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('./../')
from pages.page_base import BasePage
import os

from etc.config import BASEDIR
from tools.get_logger import MyLogger
from tools.get_data import Conf_info
LOGGER=MyLogger().get_logger_web_test()


class IndexPage(BasePage):
    """
    封装首页page类。
    方法：1.search_contact: 首页搜索功能。
          2.goto_login: 首页前往登录功能。
    """
    def search_contact(self, text):
        """
        首页搜索功能
        :param text: 搜索内容
        :return:
        """
        try:
            LOGGER.info(f'Start to search {text}')
            # 输入内容到搜索框
            message = Conf_info(os.path.join(BASEDIR,'datas/element.ini')).get_data_from_ini(node='index',key='search_input')
            LOGGER.info(message)
            ele = self._wait_element_to_click(*message)
            self._send_keys_element(text=text,ele=ele)
            # 点击百度一下
            message = Conf_info(os.path.join(BASEDIR,'datas/element.ini')).get_data_from_ini(node='index',key='search_btn')
            ele = self._wait_element_to_click(*message)
            self._click_element(ele)
            LOGGER.info(f'Search {text} success')
        except Exception as e:
            LOGGER.error(f'Search {text} failed, the reason is {e}')
            raise Exception(f'Search {text} failed')

if __name__=="__main__":
    test1=IndexPage()

    test1.search_contact('123')