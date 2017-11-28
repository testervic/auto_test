#coding:utf-8
import requests
import warnings
from common.log import *

#过滤掉警告
warnings.filterwarnings('ignore')

class requests_handle():
    #初始化
    def __init__(self, method = '', url = '', body = '', headers = '', verify = False):
        self.method = method
        self.url = url
        self.body = body
        self.headers = headers
        self.verify = verify
        self.result = None

    #设置requests参数
    def set_requests_para(self, method, url, body = '', headers = '', verify = False):
        self.method = method
        self.url = url
        self.body = body
        self.headers = headers
        self.verify = verify
        self.result = None        

    #执行request请求，支持get和post方法
    def exc_requests(self):
        #method不区分大小写
        if self.method.lower() not in ('get', 'post'):
            logging.error('暂未配置get以及post外的方法!\n\t请求方法为\t'.decode('utf-8') + str(self.method))
            return False
        elif str(self.url)[:7].lower() != 'http://' and str(self.url)[0:8].lower() != 'https://':
            logging.error('URL配置错误，请正确配置URL后使用\n\t请求URL为:\t'.decode('utf-8') + str(self.url))
            return False
        elif self.method.lower() == 'get':
            try:
                self.result = requests.get(self.url, self.verify)                
                return self.result.text
            except requests.RequestException, e:
                logging.error('request请求接口失败\n\t请求方法为:\t'.decode('utf-8') + str(self.method) + '\n\t请求URL为:\t'.decode('utf-8') + str(self.url) + '\n\t异常信息为:\t'.decode('utf-8') + str(e))
                return False
        elif self.method.lower() == 'post':
            try:
                self.result = requests.post(self.url, data = self.body, headers = self.headers, verify = self.verify)
                return self.result.text
            except requests.RequestException, e:
                logging.error('request请求接口失败\n\t请求方法为:\t'.decode('utf-8') + str(self.method) + '\n\t请求URL为:\t'.decode('utf-8') + str(self.url) + '\n\t请求Body为:\t'.decode('utf-8') + str(self.body) + '\n\t请求Headers为:\t'.decode('utf-8') + str(self.headers) + '\n\t异常信息为:\t'.decode('utf-8') + str(e))
                return False
            
            
