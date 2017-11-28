#coding:utf-8
from public.api_test.api_global import *

def get_row_value():
    # 获取excel接口数据
    excel_sheet_value = excel_sheet_value(excel_data['path'], excel_data['currency_sheet_name'])
    return excel_sheet_value

#excel数据处理
#取出excel中接口tag组成list，方便后续调用指定接口的list定位
def get_tag_list(current_sheet_value):
    tag_list = []
    if  current_sheet_value != False and len(current_sheet_value) > 1:
        for i in range(1, len(current_sheet_value)):
            tag_list.append(current_sheet_value[i][1])
        return tag_list

#获取接口数据在list中的位置
def get_list_index(tag_list,api_tag):
    return tag_list.index(api_tag)

#取返回数据中指定位置的单条接口数据
def get_api_row(excel_sheet_value, num):
    return excel_sheet_value[num]

