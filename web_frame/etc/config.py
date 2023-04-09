# -*- coding: utf-8 -*-
# @Time    : 2023/3/19 9:32
# @Author  : 石鑫磊
# @Site    : 
# @File    : config.py
# @Software: PyCharm 
# @Comment :
#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('./../')
# 项目根路径
from tools.get_project_dir import get_base_dir
BASEDIR = get_base_dir(dir_name='web_frame')
# print(BASEDIR)

##linux 信息
hostname='192.168.1.99'
name='root'
password='root'
port=22


