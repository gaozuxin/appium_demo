# -*- coding: utf-8 -*-
import datetime
import os

from BeautifulReport import BeautifulReport
from HTMLTestRunner import HTMLTestRunner
import unittest, time

from common.sendEmail import Email


def _main():
    testdir = os.path.dirname(os.path.dirname(__file__))
    test_dir = os.path.join(testdir, 'testCase')  # 测试用例文件夹
    report_dir = os.path.join(testdir, 'result/report')
    discover = unittest.defaultTestLoader.discover(test_dir, 'taskCase*.py', None)
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = '测试报告' + str(now)
    BeautifulReport(discover).report(description='测试', filename=filename, log_path=report_dir)


if __name__ == "__main__":
    _main()
