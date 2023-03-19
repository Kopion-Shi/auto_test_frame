# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 10:37
# @Author  : 石鑫磊
# @Site    :
# @File    : page_base.py
# @Software: PyCharm
# @Comment :

import os
import sys

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
sys.path.append('./../')
from etc.config import BASEDIR
from tools.get_logger import MyLogger
LOGGER=MyLogger().get_logger_web_test()
class BasePage():
    """
    公共page类，封装浏览器的相关操作方法。
    方法：1.
    _get_url: 访问网址
    2.
    _find_element: 二次封装，定位页面单个元素方法
    3.
    _find_elements: 二次封装，定位页面多个元素方法
    4.
    _click_element: 二次封装，点击页面元素的方法
    5.
    _send_keys_element: 二次封装，输入内容到页面元素的方法
    6.
    _wait_element_to_click: 二次封装，显示等待元素可点击
    7.
    _get_title: 二次封装，获取页面title
    8.
    _quit_driver: 二次封装，关闭浏览器
    9.
    _get_screenshot_as_file: 二次封装：获取页面截图并保存


    """

    def __init__(self, driver:WebDriver=None):
        """
    构造方法
    :param
    plugins:
    """
    # 生成一个driver对象
        if not driver:
            driver_path = os.path.join(BASEDIR,'plugins/chromedriver_win32/chromedriver.exe')
            self._driver = webdriver.Chrome(executable_path=driver_path)
            # self._driver.add_argument('--headless')
            # self._driver.add_argument('--no-sandbox')
            # self._driver.add_argument('--disable-gpu')
            # self._driver.add_argument('--disable-dev-shm-usage')
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def _get_url(self, url):
        """
        二次封装：访问网址方法
        :param
        url: url地址
        :return:
        """
        try:
            self._driver.get(url)
            LOGGER.info(f'visit url {url} success')
        except Exception as e:
            LOGGER.error(f'visit url {url} failed, the reason is {e}')
            raise Exception(f'visit url {url} failed')

    def _find_element(self, method, message):
        """
        二次封装，定位页面单个元素方法
        :param
        method: 定位元素的方法。例如：By.ID
        :param
        message: 元素信息。例如："kw"
        :return:
        """
        try:
            if method == "id":
                ele = self._driver.find_element(By.ID,message)
                LOGGER.info(f'find element (method:{method},message:{message}) success')
                return ele
            elif method == "name":
                ele = self._driver.find_element(By.NAME,message)
                LOGGER.info(f'find element (method:{method},message:{message}) success')
                return ele
            elif method == "xpath":
                ele = self._driver.find_element(By.XPATH,message)
                LOGGER.info(f'find element (method:{method},message:{message}) success')
                return ele
            elif method == "css":
                ele = self._driver.find_element(By.CSS_SELECTOR,message)
                LOGGER.info(f'find element (method:{method},message:{message}) success')
                return ele
            elif method == 'class':
                ele = self._driver.find_element(By.CLASS_NAME,message)
                LOGGER.info(f'find element (method:{method},message:{message}) success')
                return ele
            elif method == 'link_text':
                ele = self._driver.find_element(By.LINK_TEXT,message)
                LOGGER.info(f'find element (method:{method},message:{message}) success')
                return ele
            elif method == 'partial_link_text':
                ele = self._driver.find_element(By.PARTIAL_LINK_TEXT,message)
                LOGGER.info(f'find element (method:{method},message:{message}) success')
                return ele
            elif method == 'tag_name':
                ele = self._driver.find_element(By.TAG_NAME,message)
                LOGGER.info(f'find element (method:{method},message:{message}) success')
                return ele
        except Exception as e:
            LOGGER.error(f'find element (method:{method},message:{message}) failed, the reason is {e}')
            raise Exception(f'not find element：method={method},message={message}')

    def _find_elements(self, method, message):
        """
        二次封装，定位页面多个元素方法
        :param
        method: 定位元素的方法。例如：By.ID
        :param
        message: 元素信息。例如："kw"
        :return:
        """

        try:
            if method == "id":
                eles = self._driver.find_elements(By.ID,message)
                LOGGER.info(f'find elements (method:{method},message:{message}) success')
                return eles
            elif method == "name":
                eles = self._driver.find_elements(By.NAME,message)
                LOGGER.info(f'find elements (method:{method},message:{message}) success')
                return eles
            elif method == "xpath":
                eles = self._driver.find_elements(By.XPATH,message)
                LOGGER.info(f'find elements (method:{method},message:{message}) success')
                return eles
            elif method == "css":
                eles = self._driver.find_elements(By.CSS_SELECTOR,message)
                LOGGER.info(f'find elements (method:{method},message:{message}) success')
                return eles
            elif method == 'class':
                eles = self._driver.find_elements(By.CLASS_NAME,message)
                LOGGER.info(f'find elements (method:{method},message:{message}) success')
                return eles
            elif method == 'link_text':
                eles = self._driver.find_elements(By.LINK_TEXT,message)
                LOGGER.info(f'find elements (method:{method},message:{message}) success')
                return eles
            elif method == 'partial_link_text':
                eles = self._driver.find_elements(By.PARTIAL_LINK_TEXT,message)
                LOGGER.info(f'find elements (method:{method},message:{message}) success')
                return eles
            elif method == 'tag_name':
                eles = self._driver.find_elements(By.TAG_NAME,message)
                LOGGER.info(f'find elements (method:{method},message:{message}) success')
                return eles
        except Exception as e:
            LOGGER.error(f'find elements (method:{method},message:{message}) failed, the reason is {e}')
            raise Exception(f'not find elements：method={method},message={message}')

    def _click_element(self, ele:WebElement):
        """
        二次封装，点击页面元素的方法
        :param
        ele: 待点击的页面元素。
        :return:
        """
        try:
            ele.click()
            LOGGER.info(f'click element {ele}')
        except Exception as e:
            LOGGER.error(f'click element {ele} failed, the reason is {e}')
            raise Exception(f'click element {ele} failed')

    def _send_keys_element(self, ele:WebElement, text):
        """
        二次封装，输入内容到页面元素的方法
        :param
        ele: 页面元素。
        :param
        text: 内容
        :return:
        """
        try:
            ele.send_keys(text)
            LOGGER.info(f'send text to element {ele} success')
        except Exception as e:
            LOGGER.error(f'send text to element {ele} failed, the reason is {e}')
            raise Exception(f'send text to element {ele} failed')

    def _wait_element_to_click(self, method, message, timeout=20):
        """
        二次封装，显示等待元素可点击
        :param
        method: 定位元素的方法。例如：By.ID
        :param
        message: 元素信息。例如："kw"
        :param
        message: 超时时间，默认为20s
        :return:
        """
        try:
            if method == "id":
                ele = WebDriverWait(self._driver,timeout).until(expected_conditions.element_to_be_clickable((By.ID,message)))
                LOGGER.info(f'wait element (method:{method} message:{message}) to clickable success')
                return ele
            elif method == "name":
                ele = WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable((By.NAME, message)))
                LOGGER.info(f'wait element (method:{method} message:{message}) to clickable success')
                return ele
            elif method == "xpath":
                ele = WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable((By.XPATH, message)))
                LOGGER.info(f'wait element (method:{method} message:{message}) to clickable success')
                return ele
            elif method == "css":
                ele = WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, message)))
                LOGGER.info(f'wait element (method:{method} message:{message}) to clickable success')
                return ele
            elif method == 'class':
                ele = WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, message)))
                LOGGER.info(f'wait element (method:{method} message:{message}) to clickable success')
                return ele
            elif method == 'link_text':
                ele = WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, message)))
                LOGGER.info(f'wait element (method:{method} message:{message}) to clickable success')
                return ele
            elif method == 'partial_link_text':
                ele = WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT, message)))
                LOGGER.info(f'wait element (method:{method} message:{message}) to clickable success')
                return ele
            elif method == 'tag_name':
                ele = WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, message)))
                LOGGER.info(f'wait element (method:{method} message:{message}) to clickable success')
                return ele
        except Exception as e:
            LOGGER.error(f'wait element (method:{method} message:{message}) to clickable failed, the reason is {e}')
            raise Exception(f'wait element (method:{method} message:{message}) to clickable failed')

    def _get_title(self):
        """
        获取页面title
        :return:
        """
        try:
            title = self._driver.title
            LOGGER.info(f'get page title success, title is {title}')
            return title
        except Exception as e:
            LOGGER.error(f'get page title failed, the reason is {e}')
            raise Exception(f'get page title failed')

    def _quit_driver(self):
        """
        关闭浏览器
        :return:
        """
        try:
            self._driver.quit()
            LOGGER.info('close broswer success')
        except Exception as e:
            LOGGER.error(f'close broswer failed, the reason is {e}')
            raise Exception('close broswe failed')

    def _get_screenshot_as_file(self, path):
        """
        截取当前页面
        :param
        path: 保存为图片的路径
        :return:
        """
        try:
            self._driver.get_screenshot_as_file(path)
            LOGGER.info(f'get screenshot as file {path} success')
        except Exception as e:
            LOGGER.error(f'get screenshot as file {path} failed, the reason is {e}')
            raise Exception(f'get screenshot as file {path} failed')


