# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 10:40
# @Author  : 石鑫磊
# @Site    : 
# @File    : get_data.py
# @Software: PyCharm 
# @Comment :
import os
import json
from configparser import ConfigParser

import yaml


class Conf_info():
    def __init__(self, file_read_path,file_write_path=None):
        self.file_write_path = file_write_path
        self.file_read_path = file_read_path

    def write_yaml(self, data):
        with open(file=self.file_write_path, mode='w', encoding='utf-8') as f:
            yaml.safe_dump(data, stream=f)

    def get_data_from_yaml(self,):
        """
        获取指定yaml文件的内容
        :param path: yaml文件路径。
        :return:
        """

        with open(self.file_read_path, 'r', encoding='utf-8') as f:
            result = yaml.safe_load(f)
            return result


    def write_jison(self, data):
        with open(self.file_write_path, mode='w', encoding='utf-8') as f:
            json.dump(data, f)

    def read_jison(self):
        with open(self.file_write_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_data_from_ini(self, node, key):
        """
        封装：获取element.ini文件方法
        :self.file_read_path: ini文件路径。
        :param node: 需要查找内容所在的node。
        :param key: 需要查找内容所在的key。
        :return:
        """
        target = ConfigParser()
        target.read(self.file_read_path, encoding='utf-8')
        result = target.get(node, key)
        result = result.split('|')  # 使用"|"完成字符串分割，返回一个列表。
        return result








if __name__ == "__main__":
    # file_write_path = './test.yaml'
    # file_read_path = './test.yaml'

    pro = Conf_info(file_read_path=r'D:\00_github\autotest_frame\web_frame\datas\search_datas.yaml').get_data_from_yaml()
    print(pro)
    # pro.write_yaml(data=data)
    # print(pro.read_yaml()['user1'])
    # conf=Conf_info('autotest_frame')
    # print(conf.get_base_dir('autotest_frame'))