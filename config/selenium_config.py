#coding:utf-8
from selenium import webdriver


#流程状态控制
status_tag = {
    "status" : 1
}

driver = webdriver.Firefox()
driver.implicitly_wait(10)