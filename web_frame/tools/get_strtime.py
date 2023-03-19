# -*- coding: utf-8 -*-
# @Time    : 2023/3/19 9:31
# @Author  : 石鑫磊
# @Site    : 
# @File    : get_strtime.py
# @Software: PyCharm 
# @Comment :
# -*- coding: utf-8 -*-

from datetime import datetime

def get_now_time():
    """
    获取当前时间字符串
    :return:
    """
    now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    return now


if __name__ == "__main__":
    print(get_now_time())
