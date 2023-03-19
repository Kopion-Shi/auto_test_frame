# -*- coding: utf-8 -*-
# @Time    : 2023/3/19 9:34
# @Author  : 石鑫磊
# @Site    : 
# @File    : get_project_dir.py
# @Software: PyCharm 
# @Comment :

# -*- coding: utf-8 -*-
import os
def get_base_dir(dir_name):
    """
    获取项目根路径
    :param dir_name: 项目根目录名字。
    :return:
    """
    now_dir = os.getcwd() # 获取当前文件的路径，相当于pwd
    while True:
        now_dir_list = os.path.split(now_dir)
        now_dir = now_dir_list[0]
        if now_dir_list[1] == dir_name:
            now_dir = os.path.join(now_dir_list[0], now_dir_list[1])
            break
    return now_dir

if __name__ == "__main__":
    print(get_base_dir('web_frame'))

