# -*- coding: utf-8 -*-
# @Time    : 2023/3/19 18:05
# @Author  : 石鑫磊
# @Site    : 
# @File    : test_1.py
# @Software: PyCharm 
# @Comment :
import pytest
def test_2():
    text=['小米']
    assert text[0] in '小米_百度'

if __name__ == "__main__":
    pytest.main(["-vs", "test_1.py"])