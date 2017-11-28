#coding:utf-8
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
from time import sleep
from config.selenium_config import *
from public.selenium_test.selenium_except import driver_process_except



#driver = webdriver.Firefox()

driver.get('http://crm.guxiansheng.cn/')
'''
#XPATH
driver.find_element_by_xpath(".//*[@id='app']/div/div/form/div[1]/input").clear()
driver.find_element_by_xpath(".//*[@id='app']/div/div/form/div[1]/input").send_keys('admin')
driver.find_element_by_xpath(".//*[@id='app']/div/div/form/div[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='app']/div/div/form/div[2]/input").send_keys('123456')
driver.find_element_by_xpath(".//*[@id='app']/div/div/form/div[3]/button").click()
'''
'''
#CSS
driver.find_element_by_css_selector(".layui-input.name").clear()
driver.find_element_by_css_selector(".layui-input.name").send_keys('admin')
driver.find_element_by_css_selector(".layui-input.pass").clear()
driver.find_element_by_css_selector(".layui-input.pass").send_keys('123456')
driver.find_element_by_css_selector(".layui-btn").click()
'''
'''
#元素
driver.find_element_by_css_selector('[name="loginusername"]').clear()
driver.find_element_by_css_selector('[name="loginusername"]').send_keys('admin')
driver.find_element_by_css_selector('[name="loginpassword"]').clear()
driver.find_element_by_css_selector('[name="loginpassword"]').send_keys('123456')
driver.find_element_by_css_selector('[lay-filter="formLogin"]').click()
'''
'''
#And
driver.find_element_by_css_selector(".layui-input.name" and '[name="loginusername"]').clear()
driver.find_element_by_css_selector('[name="loginusername"]').send_keys('admin')
driver.find_element_by_css_selector('[name="loginpassword"]').clear()
driver.find_element_by_css_selector('[name="loginpassword"]').send_keys('123456')
driver.find_element_by_css_selector('[lay-filter="formLogin"]').click()
'''
'''
#鼠标事件
right_click = driver.find_element_by_css_selector(".layui-btn")
#ActionChains(driver).context_click(right_click).perform()
#ActionChains(driver).double_click(right_click).perform()
#ActionChains(driver).move_to_element(right_click).perform()
target = driver.find_element_by_css_selector('[name="loginusername"]')
ActionChains(driver).drag_and_drop(right_click, target).perform()
'''
'''
#键盘事件
driver.find_element_by_css_selector('[name="loginusername"]').clear()
driver.find_element_by_css_selector('[name="loginusername"]').send_keys('admin')
driver.find_element_by_css_selector('[name="loginusername"]').send_keys(Keys.F12)
driver.find_element_by_css_selector('[name="loginusername"]').send_keys('aaa')
driver.find_element_by_css_selector('[name="loginusername"]').send_keys(Keys.BACKSPACE)
driver.find_element_by_css_selector('[name="loginusername"]').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_css_selector('[name="loginusername"]').send_keys(Keys.CONTROL, 'x')
driver.find_element_by_css_selector('[name="loginusername"]').send_keys(Keys.CONTROL, 'v')
'''

driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").clear()')
driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").send_keys(\'admin\')')
driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").clear()')
driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").send_keys(\'123456\')')
driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[3]/button").click()')

driver_process_except('driver.find_element_by_css_selector(".show-nav" and \'[data-title="权限管理"]\').click()')
driver_process_except('driver.find_element_by_css_selector(\'[class="examine-query jur-add"]\').click()')
driver_process_except('driver.find_element_by_css_selector(".layui-input.username").clear()')
driver_process_except('driver.find_element_by_css_selector(".layui-input.username").send_keys("test权限组".decode("utf-8"))')
driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").clear()')
driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").send_keys("就是个描述".decode("utf-8"))')
'''
tags = driver_process_except('driver.find_elements_by_css_selector(".child-select")')
if tags:
    for i in tags:
        print i
        i.click()
        sleep(1)
'''
driver_process_except('driver.find_element_by_css_selector(".child-select").click()')
driver_process_except('driver.find_element_by_css_selector(".squaredFour>label").click()')
driver_process_except('driver.find_element_by_css_selector(".examine-query.add-jur-save").click()')
driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/table/tbody/tr[1]/td[4]/a[3]").click()')
driver_process_except('driver.find_element_by_css_selector(".layui-layer-btn1").click()')
#print driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").text
driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").click()')

sleep(5)
driver_process_except('driver.close()')
