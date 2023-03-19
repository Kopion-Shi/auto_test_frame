# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 11:07
# @Author  : 石鑫磊
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm 
# @Comment :
from functools import wraps
from logging import config
from web_frame.tools.get_logger import MyLogger
base_log = MyLogger().get_logger_web_test()

def black_list_find(func):
    """
    自定义装饰器：给元素定位方法增加黑名单功能
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            res = func(*args,**kwargs)
        except Exception as e:
            # 添加黑名单功能，当元素查找失败时。遍历黑名单
            config.case_log.info(f'查找元素失败，开始遍历黑名单')
            for black in self.black_list:
                black_eles = self._find_elments(*black)
                if len(black_eles) > 0:
                    black_eles[0].click()
                    config.case_log.info(f'查找黑名单元素成功')
                    return func(*args,**kwargs)
            config.case_log.error(f'遍历黑名单元素结束，未找到黑名单元素')
            raise e
        return res
    return wrapper