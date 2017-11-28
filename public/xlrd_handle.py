#coding:utf-8
import xlrd
from common.log import *

class xlrd_handle():
    #初始化Excel文件路径，sheet页名称
    def __init__(self, file_path = '', sheet_name = ''):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = None
        self.sheet = None


    #打开Excel文件
    def open_workbook(self):
        try:
            self.workbook = xlrd.open_workbook(self.file_path)
        except:
            logging.error('打开Excel文件失败.\n\tExcel文件路径为：\t'.decode('utf-8') + str(self.file_path))
            self.workbook = None
            return False
            
    #选择sheet页
    def open_sheet(self):
        try:
            self.sheet = self.workbook.sheet_by_name(self.sheet_name)
        except:
            logging.error('选取Sheet页失败.\n\tExcel文件路径为：\t'.decode('utf-8') + str(self.file_path) + '\n\t尝试打开的Sheet页名称为:\t' + str(self.sheet_name))
            self.sheet = None
            return False

    #设置Excel文件路径
    def set_file_path(self, file_path):
        self.file_path = file_path

    #设置sheet页名称
    def set_sheet_name(self, sheet_name):
        self.sheet_name = sheet_name

    #将指定sheet页中全部数据存入list返回
    def value_to_array(self):
        return_value = []
        try:
            if self.sheet.nrows > 0:
                for i in range (0, self.sheet.nrows):
                    return_value.append(self.sheet.row_values(i))
            else:
                logging.warning('sheet页 '.decode('utf-8') + str(self.sheet_name) + ' 的数据为空'.decode('utf-8'))
            return return_value
        except:
            logging.error('读取Excel数据失败.\n\tExcel文件路径为：\t'.decode('utf-8') + str(self.file_path) + '\n\t尝试读取的Sheet页数据为:\t'.decode('utf-8') + str(self.sheet_name))
            return False

                
