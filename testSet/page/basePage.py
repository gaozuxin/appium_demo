# -*- coding: utf-8 -*-
"""
    @desc: object测试基类
    @file: base_page.py
    @date: 2019/05/08
"""
import os
import time
from selenium.common.exceptions import NoSuchElementException

from common.myCmd import excute_cmd
from common.myLogger import logger
from testSet.utils.driverSet import driver_app
from testSet.utils.inputMethod import InputMethod

UI_WAIT_TIME = 20


class BasePage(object):

    def __init__(self, driver_app):
        self._driver = driver_app
        # self._driver.implicitly_wait(10)

    def findXpath(self, loc):
        try:
            el = self._driver.find_element_by_xpath(loc)
        except(NoSuchElementException):
            logger.error('[{}]寻找元素失败, 定位方式为xpath:{}'.format(os.path.basename(__file__), loc))
            raise NoSuchElementException(msg='[{}]寻找元素失败, 定位方式为xpath:{}'.format(os.path.basename(__file__), loc))
        return el

    def findId(self, loc):
        try:
            el = self._driver.find_element_by_id(loc)
        except(NoSuchElementException):
            logger.error('[{}]寻找元素失败, 定位方式为id:{}'.format(os.path.basename(__file__), loc))
            raise NoSuchElementException(msg='[{}]寻找元素失败, 定位方式为id:{}'.format(os.path.basename(__file__), loc))
        return el

    def findAndroidUiautomator(self, text):
        try:
            el = self._driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(text))
        except(NoSuchElementException):
            logger.error('[{}]寻找元素失败, 定位方式为uiautomator:{}'.format(os.path.basename(__file__), text))
            raise NoSuchElementException(msg='[{}]寻找元素失败, 定位方式为uiautomator:{}'.format(os.path.basename(__file__), text))
        return el

    def inputById(self, loc, value):
        self.sendKeys(self.findId(loc), value)

    def inputByXpath(self, loc, value):
        self.sendKeys(self.findXpath(loc), value)

    def inputByUiautomator(self, text, value):
        self.sendKeys(self.findAndroidUiautomator(text), value)

    def clickById(self, loc):
        self.findId(loc).click()

    def clickByXpath(self, loc):
        self.findXpath(loc).click()

    def clickByUiautomator(self, text):
        self.findAndroidUiautomator(text).click()

    # 重写定义send_keys方法
    def sendKeys(self, el, vaule, clear_first=True, click_first=True):
        try:
            if click_first:
                el.click()
            if clear_first:
                el.clear()
                el.send_keys(vaule)
        except (NoSuchElementException) as e:
            logger.error("[{}]页面中未能找到元素{}".format(os.path.basename(__file__), e))
            raise NoSuchElementException(msg='[{}]页面中未能找到元素{}'.format(os.path.basename(__file__), e))

    # 截图，保存在根目录下的screenshots
    def takeScreenshot(self):
        rq = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        try:
            self._driver.get_screenshot_as_file(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                                                + r'\result\screenshots\{}.png'.format(rq))
            logger.info("[{}]已截屏并保存{}.png!".format(os.path.basename(__file__), rq))
        except Exception as e:
            logger.error("[{}]无法截屏!{}".format(os.path.basename(__file__), e))

    def getSize(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        return (x,y)


if __name__ == "__main__":
    pg = BasePage(driver_app)
    # print(pg.getSize())
    driver_app.find_element_by_id("com.yunke.enterprisep:id/ll_tab_customer").click()
    time.sleep(1)
    pg.findId("com.yunke.enterprisep:id/tv_found").click()
    driver_app.tap([(55, 204), (1025, 314)], 500)
    time.sleep(1)
    # 使用adb shell切换输入法 - 更改为谷歌输入法
    # excute_cmd("adb shell ime set com.google.android.inputmethod.pinyin/.PinyinIME")
    pg.inputById("com.yunke.enterprisep:id/et_search_customer", "高祖新-gao")
    #  再次切回 输入法键盘为Appium unicodeKeyboard，方便下次输入中文
    # excute_cmd("adb shell ime set io.appium.android.ime/.UnicodeIME")