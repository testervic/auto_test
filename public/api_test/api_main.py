#coding:utf-8
from config.api_config import *
from public.requests_handle import *
from public.xlrd_handle import *
from api_global import *
from public.common.common import *

#通用接口处理
def api_currency_requests():
    
    #实例化requests_handle
    api_requests = requests_handle()
    #取指定sheet所有数据
    current_sheet_value = excel_sheet_value(excel_data['path'], excel_data['currency_sheet_name'])

    #当前执行状态，如果通用接口执行存在错误，则不再执行其他接口
    current_status = 1

    #返回数据大于1行，则处理数据；否则判断currency页返回数据无相关接口数据
    if  current_sheet_value != False and len(current_sheet_value) > 1:
        for i in range(1, len(current_sheet_value)):
            #获取格式转换好的Excel单行数据
            request_value = excel_row_handle(current_sheet_value[i])

            if current_status == 1:
                if request_value != False:
                    #若当前接口执行出错，再执行一次该接口
                    #current_exc_time = 1

                    logging.info('接口处理参数记录.\n\t接口介绍:\t' + request_value['instruction'] + '\n\t接口标识:\t' + request_value['tag'] + '\n\t请求方式:\t' + request_value['method'] + '\n\tURL:\t' + request_value['url'] + '\n\tBody:\t' + str(request_value['body']) + '\n\tHeaders:\t' + str(request_value['headers']))
                    api_requests.set_requests_para(request_value['method'],request_value['url'],request_value['body'],request_value['headers'])
                    return_data = str_to_json(api_requests.exc_requests())

                    if return_data != False:

                        #处理所有通用接口特殊处理
                        if request_value['tag'] in ('00000001','00000002'):
                            if request_value['tag'] == '00000001' and return_data['code'] == 1:
                                currency['member_id'] = return_data['data']['member_id']
                                currency['key'] = return_data['data']['key']
                            elif request_value['tag'] == '00000002' and return_data['code'] == 1:
                                currency['hashkey'] = return_data['data']['member_id']
                            else:
                                logging.error('通用接口处理失败.\n\t接口介绍:\t' + request_value['instruction'] + '\n\t接口标识:\t' + request_value['tag'] + '\n\t请求方式:\t' + request_value['method'] + '\n\tURL:\t' + request_value['url'] + '\n\tBody:\t' + str(request_value['body']) + '\n\tHeaders:\t' + str(request_value['headers']) + '\n\t接口返回数据:\t'.decode('utf-8') + str(return_data))
                                #通用接口处理失败，直接退出循环退出
                                current_status = 0
                                break
                        else:
                            logging.error('通用接口操作行请求返回数据不包含所需数据,直接退出测试'.decode('utf-8'))
                            # 如果通用接口数据报错，直接退出循环退出
                            current_status = 0
                            break
                    else:
                        logging.error('通用接口操作行请求返回数据异常,直接退出测试'.decode('utf-8'))
                        # 如果通用接口数据报错，直接退出循环退出
                        current_status = 0
                        break
                else:
                    logging.error('通用接口操作行请求使用数据异常,直接退出测试'.decode('utf-8'))
                    # 如果通用接口数据报错，直接退出循环退出
                    current_status = 0
                    break

    #通用接口处理失败，返回False
    if current_status == 0:
        return False

def api_common_requests():
    # 实例化requests_handle
    api_requests = requests_handle()
    # 取指定sheet所有数据
    current_sheet_value = excel_sheet_value(excel_data['path'], excel_data['common_sheet_name'])

    # 返回数据大于1行，则处理数据；否则判断common页返回数据无相关接口数据
    if current_sheet_value != False and len(current_sheet_value) > 1:
        for i in range(1, len(current_sheet_value)):
            # 获取格式转换好的Excel单行数据
            request_value = excel_row_handle(current_sheet_value[i])

            # 若当前接口执行出错，重新轮询通用接口后，再执行一次该接口
            current_exc_time = 1

            while current_exc_time <= 2:
                if request_value != False:
                    logging.info('接口处理参数记录.\n\t接口介绍:\t' + request_value['instruction'] + '\n\t接口标识:\t' + request_value[ 'tag'] + '\n\t请求方式:\t' + request_value['method'] + '\n\tURL:\t' + request_value['url'] + '\n\tBody:\t' + str(request_value['body']) + '\n\tHeaders:\t' + str(request_value['headers']))
                    api_requests.set_requests_para(request_value['method'], request_value['url'], request_value['body'],request_value['headers'])
                    return_data = str_to_json(api_requests.exc_requests())

                    if return_data != False:

                        #接口返回数据判断
                        if request_value['tag'] not in ('00000002'):
                            if return_data['code'] == 1:
                                logging.info('接口轮询记录.\n\t接口介绍:\t' + request_value['instruction'] + '\n\t接口标识:\t' + request_value['tag'] + '\t轮询成功')
                                current_exc_time = 99
                            elif return_data['code'] != 1 and current_exc_time == 1:
                                logging.error('接口处理失败.\n\t接口介绍:\t' + request_value['instruction'] + '\n\t接口标识:\t' + request_value['tag'] + '\n\t请求方式:\t' + request_value['method'] + '\n\tURL:\t' + request_value['url'] + '\n\tBody:\t' + str(request_value['body']) + '\n\tHeaders:\t' + str(request_value['headers']) + '\n\t接口返回数据:\t'.decode('utf-8') + str(return_data) + '\n\t第' + str(current_exc_time) + '次轮询失败，再次执行通用接口')
                                current_exc_time += 1
                                currency_result = api_currency_requests()
                                if currency_result is False:
                                    break
                                print currency
                            else:
                                logging.error('接口处理失败.\n\t接口介绍:\t' + request_value['instruction'] + '\n\t接口标识:\t' + request_value['tag'] + '\n\t请求方式:\t' + request_value['method'] + '\n\tURL:\t' + request_value['url'] + '\n\tBody:\t' + str(request_value['body']) + '\n\tHeaders:\t' + str(request_value['headers']) + '\n\t接口返回数据:\t'.decode('utf-8') + str(return_data) + '\n\t第' + str(current_exc_time) + '次轮询失败，跳过当前接口')
                                current_exc_time = 99
                        else:
                            logging.info('我在这里')
                            current_exc_time = 99
                    else:
                        logging.info('看这里')
                        current_exc_time = 99

                else:
                    logging.info('Excel中的操作行请求数据异常,跳过该行'.decode('utf-8'))
                    current_exc_time = 99
