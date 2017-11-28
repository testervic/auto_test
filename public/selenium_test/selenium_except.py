#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.selenium_config import *
from time import sleep

#流程异常处理
def driver_process_except(driver_process_str, driver = driver ,loop_num = 10, sleep_time = 1,tag = status_tag):
    if tag['status'] == 1:
        print 'Current Process : ' + str(driver_process_str)
        num = 0
        while num < loop_num:
            #print num
            try:
                exec('temp_result = ' + driver_process_str)
            except Exception,e:
                print e
            else:
                break
            finally:
                num += 1
                sleep(sleep_time)
        if num == loop_num:
            tag['status'] = 0
            return False
        else:
            return temp_result