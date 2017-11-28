#coding:utf-8
import unittest
from time import sleep
from config.selenium_config import *
from public.selenium_test.selenium_except import driver_process_except
from config.api_config import hosts_config
from public.common.common import modify_hosts


class CRM_Process(unittest.TestCase):

    driver = driver

    def __init__(self,methodName='runTest'):
        super(CRM_Process, self).__init__(methodName)

    @classmethod
    def setUpClass(cls):
        #modify_hosts(hosts_config['Intranet'])
        pass

    @classmethod
    def tearDownClass(cls):
        #modify_hosts(hosts_config['Extranet'])
        pass

    def check_process_status(self):
        self.assertEqual(status_tag['status'], 1)

    #浏览器打开CRM
    def test_open_url(self):
        #driver_process_except('driver.get("http://crm.guxiansheng.cn/")')
        driver_process_except('driver.get("http://crm.guxiansheng.cn/admin/auth/group")')
        self.check_process_status()

    #CRM登录
    def test_login(self):
        self.check_process_status()
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").clear()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").send_keys(\'admin\')')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").clear()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").send_keys(\'123456\')')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[3]/button").click()')
        self.check_process_status()

    #CRM权限管理
    def test_power_manager(self):

        self.check_process_status()
        driver_process_except('driver.find_element_by_css_selector(".show-nav" and \'[data-title="权限管理"]\').click()')
        driver_process_except('driver.find_element_by_css_selector(\'[class="examine-query jur-add"]\').click()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input.username").clear()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input.username").send_keys("testpowergroup")')
        driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").clear()')
        driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").send_keys("descriptiondescriptiondescription")')
        driver_process_except('driver.find_element_by_css_selector(".child-select").click()')
        driver_process_except('driver.find_element_by_css_selector(".squaredFour>label").click()')
        driver_process_except('driver.find_element_by_css_selector(".examine-query.add-jur-save").click()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input").clear()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input").send_keys("testpowergroup")')
        driver_process_except('driver.find_element_by_css_selector(".examine-query").click()')
        self.assertEqual(driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/table/tbody/tr/td[1]").text'), 'testpowergroup')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/table/tbody/tr[1]/td[4]/a[3]").click()')
        driver_process_except('driver.find_element_by_css_selector(".layui-layer-btn1").click()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").click()')
        self.check_process_status()

    def test_driver_close(self):
        sleep(5)
        driver_process_except('driver.close()')
        self.check_process_status()
