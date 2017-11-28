#coding:utf-8
from config.api_config import *
from ..common.log import *
from ..common.common import *
from public.xlrd_handle import *

#excel中单元格数据的参数替换处理
#将单元格中包含在||内的变量转成对应参数，替换参数均统一保存在common_data字典中
def var_convert_para(need_convert):

    try:
        temp_str = str(need_convert)
    except:
        logging.error('变量转换参数失败.转为str类型处理失败'.decode('utf-8'))
        return False

    #将str以'|'为分隔符，转成list
    temp_list = temp_str.split('|')

    #list长度大于1时，开始转换
    if len(temp_list) > 1:
        for i in range(0, len(temp_list)):
            #所有待替换的变量位置均为list的奇数位
            if i % 2 == 1:
                try:
                    temp_list[i] = common_data[temp_list[i]]
                except:
                    logging.error('参数替换失败.\n\t替换的变量为:\t'.decode('utf-8') + str(temp_list[i]))
                    return False
        #将替换好的str返回
        return ''.join(temp_list)
                
    else:
        return temp_str
        

#参数为excel中任意行的接口数据,list格式,处理为可使用的字典格式返回
def excel_row_handle(row_value):

    request_value = {}
    request_value['instruction'] = row_value[0]
    request_value['tag'] = row_value[1]
    request_value['interfacestatus'] = row_value[2]
    request_value['method'] = row_value[3]
    request_value['url'] = row_value[4]
    #body参数替换并转为json格式
    temp_body_value = var_convert_para(row_value[5])
    if temp_body_value != False:
        temp_body_json = str_to_json(temp_body_value)
        if temp_body_json != False:
            request_value['body'] = temp_body_json
        else:
            logging.error( '接口 '.decode('utf-8') + request_value['instruction'] + ':' + request_value['tag'] + ' Body数据json格式转换异常'.decode('utf-8'))
            return False
    else:
        logging.error('接口 '.decode('utf-8') + request_value['instruction'] + ':' + request_value['tag'] + ' Body数据参数替换异常'.decode('utf-8'))
        return False
    #headers转为json格式
    temp_headers_json = str_to_json(row_value[6])
    if temp_headers_json != False:
        request_value['headers'] = temp_headers_json
    else:
        logging.error( '接口 '.decode('utf-8') + request_value['instruction'] + ':' + request_value['tag'] + ' headers数据json格式转换异常'.decode('utf-8'))
        return False

    request_value['checkpoint'] = row_value[7]

    return request_value

#获取指定路径和指定sheet名称的sheet页的全部数据
def excel_sheet_value(path, sheet_name):

    # 实例化xlrd_handle
    sheet_obj = xlrd_handle(path, sheet_name)

    workbook_status = sheet_obj.open_workbook()
    if workbook_status == False:
        return False
    sheet_status = sheet_obj.open_sheet()
    if sheet_status == False:
        return  False

    # 获取指定sheet页中的全部数据，并返回
    sheet_value = sheet_obj.value_to_array()
    return sheet_value