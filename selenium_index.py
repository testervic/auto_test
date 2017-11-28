#coding:utf-8
import HTMLTestRunner
from public.selenium_test.CRM.CRM_Process import CRM_Process
from public.common.sendEmail import send_email_report
from config.email_config import email_config
import unittest
import datetime
import os
import re

if __name__ == '__main__':
    #设置测试用例组件
    suite = unittest.TestSuite()
    #用例流程添加
    tests = [CRM_Process("test_open_url"), CRM_Process("test_login"), CRM_Process("test_power_manager"), CRM_Process("test_driver_close")]
    suite.addTests(tests)

    #设置报告路径
    date_str = str(datetime.datetime.now()).split('.')[0]
    report_file_path = os.getcwd() + '\\report\\HTMLReport' + re.sub('[- :]', '', date_str) + '.html'

    #用例执行，生成报告
    with open(report_file_path, 'w') as report_f:
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=report_f,
                    title='CRM',
                    description='generated by HTMLTestRunner.',
                    verbosity=2
                )
        runner.run(suite)
    '''
    #邮件发送
    email_config['receiver'] = 'liuxu@guxiansheng.cn'
    email_config['attachment'] = [report_file_path]
    email_config['mail_body'] = 'CRM权限管理自动化测试报告'
    send_email_report(email_config)
    '''
