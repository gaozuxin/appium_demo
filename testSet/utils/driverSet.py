# -*- coding: utf-8 -*-
from appium import webdriver
import os
from common.myLogger import logger


class Driver(object):
    def __init__(self):
        self.device_name = None
        pipeline = os.popen("adb devices")  # cmd获取设备名称
        adb_version = os.popen("adb shell getprop ro.build.version.release")  # cmd获取Android系统版本
        adb_devices = pipeline.read()
        try:
            self.device_name = adb_devices.split()[4]
        except Exception as msg:
            logger.error("请检查移动设备是否连接正常,异常信息{}".format(msg))
            raise

        # 初始化信息
        self.desired_caps ={}
        self.desired_caps["platformName"] = "Android"
        self.desired_caps["platformVersion"] = adb_version = adb_version.read()
        self.desired_caps["deviceName"] = self.device_name
        self.desired_caps["appPackage"] = "com.yunke.enterprisep"
        self.desired_caps["appActivity"] = ".module.main.MainActivity"
        self.desired_caps["unicodeKeyboard"] = True  # 隐藏手机中的软键盘
        self.desired_caps["resetKeyboard"] = True
        self.desired_caps["noReset"] = True

        # desired_caps = {"platformName": "Android",
        #                 "platformVersion": adb_version,
        #                 "deviceName": self.device_name,
        #                 "appPackage": "com.yunke.enterprisep",
        #                 "appActivity": ".module.main.MainActivity",
        #                 "unicodeKeyboard": True,
        #                 "resetKeyboard": True,
        #                 "noReset": True
        # }

        logger.info("[{}]driver初始化‖platformVersion:{},deviceName:{}".format(os.path.basename(__file__),
                                                                             adb_version, self.device_name))

    # drvier_app.start_activity("com.yunke.enterprisep", ".module.main.MainActivity")
    def connect(self, port=4723):
        url = 'http://localhost:%s/wd/hub' % str(port)
        try:
            driver = webdriver.Remote(url, self.desired_caps)
            logger.info("[{}]启动接口为:{},手机ID为：{}".format(os.path.basename(__file__),
                                                       port, self.device_name))
        except Exception as msg:
            logger.error("[{}]appium启动失败,请检查appium服务是否开启；异常原因:{}".format(os.path.basename(__file__), msg))
            os.popen("taskkill /f /im adb.exe")
            raise
        return driver


driver_app = Driver().connect()