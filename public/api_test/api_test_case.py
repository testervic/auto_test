#coding:utf-8
import unittest
import sys
from public.common.common import *
from public.api_test.api_test_base import *
from public.api_test.api_global import *
from config.api_config import *
import sys

class apiTestCase(unittest.TestCase):

    excel_sheet_value = excel_sheet_value(excel_data['path'], excel_data['currency_sheet_name'])

    def __init__(self,methodName='runTest',tag = None,skip = 0):
        super(apiTestCase, self).__init__(methodName)
        self.excel_sheet_value = apiTestCase.excel_sheet_value
        self.api_tag_list = get_tag_list(self.excel_sheet_value)
        self.tag = tag
        self.skip = skip
        if self.skip:
            fun_str = 'test_' + str(self.tag)
            fun_temp_create = 'def {fun_name}(self): print 111'
            exec(fun_temp_create.format(fun_name = fun_str))
        #self.no = apiTestCase.no


    @classmethod
    def setUpClass(cls):
        #测试环境hosts配置
        modify_hosts(hosts_config['Extranet'])

    @classmethod
    def tearDownClass(cls):
        #测试环境host恢复
        modify_hosts(hosts_config['Extranet'])


    def test_show(self):
        print 1234
        print self.api_tag_list
        #print apiTestCase.no

    def test_111(self):
        print self.excel_sheet_value
        print apiTestCase.aaa

    def test_row(self):
        print get_api_row(self.excel_sheet_value, 2)

    def test_api_index(self):
        print get_list_index.__name__
        print get_list_index(self.api_tag_list, self.tag)


    def test_00000001(self):
        self.assertIn(self.tag, self.api_tag_list)
        #self.request_value = excel_row_handle(self.excel_sheet_value[get_list_index(self.api_tag_list, '00000001')])
        self.assertNotEquals(excel_row_handle(self.excel_sheet_value[get_list_index(self.api_tag_list, self.tag)]), False)

        print self.request_value

    @staticmethod
    def loop_create_function(list_fun_name):
        if type(list_fun_name) is list:
            for i in (list_fun_name):
                fun_temp_create = 'def {fun_name}(self): self.assertNotEquals(excel_row_handle(self.excel_sheet_value[get_list_index(self.api_tag_list, self.tag)]), False)'
                exec(fun_temp_create.format(fun_name = 'test_' + str(i)))
        else:
            print '创建方法失败'.decode('utf-8')
            return 0



