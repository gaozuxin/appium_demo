# -*- coding: utf-8 -*-
import sys
import time
import unittest
import warnings

from common.myLogger import logger
from testSet.utils.driverSet import driver_app
from testSet.page.basePage import BasePage


class TaskCase0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        cls.pg = BasePage(driver_app)
        logger.info("{}{}start{}".format("*"*25, __name__, "*"*25))
        # driver_app.implicitly_wait(8)
        # driver_app.findId("com.yunke.enterprisep:id/et_phone").click()
        # driver_app.findId("com.yunke.enterprisep:id/et_phone").send_keys("mengtian-02")
        # driver_app.findId("com.yunke.enterprisep:id/tv_next").click()
        # driver_app.findId("com.yunke.enterprisep:id/et_password").click()
        # driver_app.findId("com.yunke.enterprisep:id/et_password").send_keys("111111")
        # driver_app.findId("com.yunke.enterprisep:id/tv_login").click()

    @classmethod
    def tearDownClass(cls):
        # mysql.close()
        logger.info("************************************{}end*************************************".format(__name__))

    def setUp(self):
        pass

    def tearDown(self):
        self.pg.takeScreenshot()

    # @unittest.skip
    # @fail_run(n)
    def test_customer_001(self):
        """给客户打电话"""
        logger.info("*{}用例{}\{}开始执行{}*".format("=" * 20, __name__, sys._getframe().f_code.co_name, "=" * 20))
        driver_app.start_activity("com.yunke.enterprisep", ".module.main.MainActivity")  # 启动Activity
        self.pg.findAndroidUiautomator("管客户").click()
        self.pg.findId('com.yunke.enterprisep:id/iv_phone').click()  # 点击拨打电话按钮
        time.sleep(1)
        self.pg.takeScreenshot()
        time.sleep(2)
        self.pg.findId('com.android.dialer:id/floating_end_call_action_button').click()  # 点击挂断电话按钮
        time.sleep(0.5)
        self.pg.takeScreenshot()
        # self.assertEqual('gaozuxin', islogin, msg="注册并登录失败")
        logger.info("*{}用例{}\{}执行结束{}*".format("="*20, __name__, sys._getframe().f_code.co_name, "="*20))

    # @unittest.skip
    # @fail_run(n)
    def test_customer_002(self):
        """添加客户"""
        logger.info("*{}用例{}\{}开始执行{}*".format("=" * 20, __name__, sys._getframe().f_code.co_name, "=" * 20))
        driver_app.start_activity("com.yunke.enterprisep", ".module.main.MainActivity")  # 启动Activity
        self.pg.findAndroidUiautomator("管客户").click()
        self.pg.findAndroidUiautomator("添加").click()
        self.pg.findAndroidUiautomator("录入客户").click()
        self.pg.findAndroidUiautomator("请输入姓名").click()
        self.pg.findAndroidUiautomator("录入客户").click()
        # self.pg.findAndroidUiautomator("请输入姓名").send_keys("gaozuxin")
        self.pg.sendKeys(self.pg.findAndroidUiautomator("请输入姓名"), "gaozuxin")
        self.pg.findAndroidUiautomator("请输入手机").click()
        # self.pg.findAndroidUiautomator("请输入手机").send_keys("18637607203")
        self.pg.sendKeys(self.pg.findAndroidUiautomator("请输入手机"), "18637607403")
        # self.pg.findAndroidUiautomator("请输入手机").send_keys("18637607203")
        try:
            self.pg.findAndroidUiautomator("请输入邮箱").click()
            # self.pg.findAndroidUiautomator("请输入邮箱").send_keys("gaozuxin@tojoy.com")
            self.pg.sendKeys(self.pg.findAndroidUiautomator("请输入邮箱"), "gaozuxin@tojoy.com")
            self.pg.findAndroidUiautomator("请输入QQ").click()
            # self.pg.findAndroidUiautomator("请输入QQ").send_keys("120983257")
            self.pg.sendKeys(self.pg.findAndroidUiautomator("请输入QQ"), "120983257")
        except Exception as msg:
            print("异常原因" + str(msg))
        self.pg.findAndroidUiautomator("请输入微信号").click()
        # self.pg.findAndroidUiautomator("请输入微信号").send_keys("XIN507197")
        self.pg.sendKeys(self.pg.findAndroidUiautomator("请输入微信号"), "XIN507197")
        self.pg.findAndroidUiautomator("请输入职位").click()
        # self.pg.findAndroidUiautomator("请输入职位").send_keys("tester")
        self.pg.sendKeys(self.pg.findAndroidUiautomator("请输入职位"), "tester")
        self.pg.findAndroidUiautomator("请选择性别").click()
        self.pg.findAndroidUiautomator("确定").click()
        self.pg.findAndroidUiautomator("保存").click()
        # self.assertEqual('gaozuxin', islogin, msg="注册并登录失败")
        logger.info("*{}用例{}\{}执行结束{}*".format("=" * 20, __name__, sys._getframe().f_code.co_name, "=" * 20))

    # @unittest.skip
    # @fail_run(n)
    # def test_customer_003(self):
    #     """编辑用户资料"""
    #     logger.info("*{}用例{}\{}开始执行{}*".format("=" * 20, __name__, sys._getframe().f_code.co_name, "=" * 20))
    #     driver_app.start_activity("com.yunke.enterprisep", ".module.main.MainActivity")  # 启动Activity
    #     driver_app.findAndroidUiautomator("管客户").click()
    #     driver_app.findId('com.yunke.enterprisep:id/iv_phone').click()  # 点击拨打电话按钮
    #     driver_app.findId('com.android.dialer:id/videoCallFragment').click()  # 点击挂断电话按钮
    #     # self.assertEqual('gaozuxin', islogin, msg="注册并登录失败")
    #     logger.info("*{}用例{}\{}执行结束{}*".format("="*20, __name__, sys._getframe().f_code.co_name, "="*20))


if __name__ == '__main__':
    unittest.main()
