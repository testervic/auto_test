#coding:utf-8
from public.common.date import *
from public.common.common import *
from public.mysql_handle import *
from public.report.report_currency import *

#神预算统计数据方式配置
divine_budget_config = {
    #股机板块对应的时间段内，发布的股机中包含该股票
    "gj":{
        "condition1":(10, '股机A包含一次，神力值 + 10'),
        "condition2":(20, '股机B包含一次，神力值 + 20'),
        "condition3":(30, '股机C包含一次，神力值 + 30')
    },
    #擒牛诀板块对应的时间段内，发布的擒牛诀包含该股票
    "qnj":{
        "condition1":(20, '擒牛决包含一次且星级5，神力值 + 20'),
        "condition2":(10, '擒牛决包含一次且星级3~4，神力值 + 10'),
        "condition3":(5, '擒牛决包含一次且星级1~2，神力值 + 5')
    },
    #股池板块对应的时间段内，运作中的股池买入卖出该股票;整体仓位是指个股市值与该股池总资产的比值
    "gc":{
        "condition1":(30, '股池买入一次，且整体仓位为80%~100%，神力值 + 30'),
        "condition2":(20, '股池买入一次，且整体仓位为60%~79%，  神力值 + 20'),
        "condition3":(5, '股池买入一次，且整体仓位小于59%，神力值 + 5'),
        "condition4":(-20, '股池卖出一次，且清仓卖出，神力值 - 20'),
        "condition5":(-15, '股池卖出一次，且卖出股数占比为60%~99%，神力值 - 15'),
        "condition6":(-10, '股池卖出一次，且卖出股数占比小于59%，神力值 - 10'),
        "condition7":(-5, '股池卖出一次，且卖出股数占比小于59%，神力值 - 5')
    },
    #锦囊板块对应的时间段内，发布的锦囊包含该股票
    "jn":{
        "condition1": (40, '锦囊包含一次，神力值 + 40'),
        "condition2":(-20, '锦囊提前止盈，神力值 - 20'),
        "condition3":(-20, '锦囊提前止损，神力值 - 20')
    },
    #第三方服务
    "sf":{
        "condition1": (50, '涨停风云中发布的文章包含一次，神力值 + 50'),
        "condition2":(-30, '涨停风云中发布的文章状态变更为“已出局”， 神力值 - 30'),
        "condition3":(70, '主升传奇中发布的文章包含一次，神力值 + 70'),
        "condition4":(-35, '主升传奇中发布的文章状态变更为“已出局”， 神力值 - 35')
    },
    #自选股板块对应的时间段内，添加或取消该股票 （此处过滤新股，带新股标签的股票不计算神力值增减）
    "zxg":{
        "condition1": (1, '自选股版块每添加一次，神力值 + 1'),
        "condition2":(-1, '自选股版块每取消一次，神力值 - 1')
    }
}

#中间所有积分修改记录保存
temp_value = []

#股机神力值处理
def add_gj(db_link,date_time):
    sql = 'SELECT SUBSTR(a.stock_code,-6),b.plan_class_id,FROM_UNIXTIME(time) FROM stock_plan_stock a INNER JOIN stock_plan b ON a.plan_id = b.id WHERE b.status = 1 AND time >= UNIX_TIMESTAMP(\'' + date_time[0] + '\') AND time < UNIX_TIMESTAMP(\'' + date_time[1] + '\')'
    sql_result = db_link.exc_sql(sql)
    if sql_result[0] > 0:
        for i in range(0, sql_result[0]):
            current_value = []
            #股机A包含
            if sql_result[1][i][1] == 85:
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['gj']['condition1'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['gj']['condition1'][1])
            #股机B包含
            elif sql_result[1][i][1] == 86:
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['gj']['condition2'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['gj']['condition2'][1])
            #股机C包含
            elif sql_result[1][i][1] == 87:
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['gj']['condition3'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['gj']['condition3'][1])
            temp_value.append(current_value)

#擒牛决神力值处理
def add_qnj(db_link,date_time):
    sql = 'SELECT a.stock_code,a.`level`,FROM_UNIXTIME(time) FROM stock_report_stock a INNER JOIN stock_report_article b on a.report_id = b.report_id WHERE b.`status` = 1 AND b.time >= UNIX_TIMESTAMP(\'' + date_time[0] + '\') AND b.time < UNIX_TIMESTAMP(\'' + date_time[1] + '\')'
    sql_result = db_link.exc_sql(sql)
    if sql_result > 0:
        for i in range(0, sql_result[0]):
            current_value = []
            #包含一次且星级5
            if sql_result[1][i][1] == 5:
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['qnj']['condition1'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['qnj']['condition1'][1])
            #包含一次且星级3~4
            elif sql_result[1][i][1] in (3, 4):
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['qnj']['condition2'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['qnj']['condition2'][1])
            #包含一次且星级1~2
            elif sql_result[1][i][1] in (1, 2):
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['qnj']['condition3'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['qnj']['condition3'][1])
            temp_value.append(current_value)

#股池神力值处理
def add_gc(db_link,date_time):
    pass

#锦囊神力值处理
def add_jn(db_link,date_time):
    #发布情况处理
    sql = 'SELECT SUBSTR(stock_code,-6),FROM_UNIXTIME(time) FROM stock_jn WHERE time >= UNIX_TIMESTAMP(\'' + date_time[0] + '\') AND time < UNIX_TIMESTAMP(\'' + date_time[1] + '\')'
    sql_result = db_link.exc_sql(sql)
    if sql_result[0] > 0:
        for i in range(0, sql_result[0]):
            current_value = []
            #发布即增加指定神力值
            current_value.append(sql_result[1][i][0])
            current_value.append(divine_budget_config['jn']['condition1'][0])
            current_value.append(str(sql_result[1][i][1]) + ' ' + divine_budget_config['jn']['condition1'][1])
            temp_value.append(current_value)
    #提前止盈和提前止损处理
    sql = 'SELECT SUBSTR(stock_code,-6),finish_status,FROM_UNIXTIME(finish_time) FROM stock_jn WHERE finish_status IN (1, 4) and finish_time >= UNIX_TIMESTAMP(\'' + date_time[0] + '\') AND finish_time < UNIX_TIMESTAMP(\'' + date_time[1] + '\')'
    sql_result = db_link.exc_sql(sql)
    if sql_result[0] > 0:
        for i in range(0, sql_result[0]):
            current_value = []
            #锦囊提前止盈
            if sql_result[1][i][1] == 1:
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['jn']['condition2'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['jn']['condition2'][1])
            #锦囊提前止损
            elif sql_result[1][i][1] == 4:
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['jn']['condition3'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['jn']['condition3'][1])
            temp_value.append(current_value)

#第三方神力值处理
def add_sf(db_link,date_time):
    #添加情况处理
    sql = 'SELECT a.stock_code,c.service_code,FROM_UNIXTIME(a.add_time) FROM stock_agency_service_stock a INNER JOIN stock_agency_service  b ON b.service_id = a.service_id INNER JOIN stock_agency_service_class c ON c.asc_id = b.asc_id WHERE c.service_code in (\'ztfy\',\'zscq\') AND a.stock_code <> \'\' AND add_time >= UNIX_TIMESTAMP(\'' + date_time[0] + '\') AND add_time < UNIX_TIMESTAMP(\'' + date_time[1] + '\')'
    sql_result = db_link.exc_sql(sql)
    if sql_result[0] > 0:
        for i in range(0, sql_result[0]):
            current_value = []
            #涨停风云发布包含
            if sql_result[1][i][1] == 'ztfy':
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['sf']['condition1'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['sf']['condition1'][1])
            #主升传奇发布包含
            elif sql_result[1][i][1] == 'zscq':
                current_value.append(sql_result[1][i][0])
                current_value.append(divine_budget_config['sf']['condition3'][0])
                current_value.append(str(sql_result[1][i][2]) + ' ' + divine_budget_config['sf']['condition3'][1])
            temp_value.append(current_value)
    #出局情况处理需补充，等开发记录出局时间后添加


#自选股神力值处理
def add_zxg(db_link,date_time):
    #处理自选股指定时间内添加统计
    sql = 'SELECT SUBSTR(stock_member_stock.stock_code,-6),COUNT(*) FROM stock_member_stock WHERE SUBSTR(stock_code,-8,2) NOT IN (\'sz\',\'sh\') AND time > UNIX_TIMESTAMP(\'' + date_time[0] + '\') AND time <= UNIX_TIMESTAMP(\'' + date_time[1] + '\') GROUP BY stock_code'
    sql_result = db_link.exc_sql(sql)
    if sql_result[0] > 0:
        for i in range(0, sql_result[0]):
            current_value = []
            current_value.append(sql_result[1][i][0])
            current_value.append(sql_result[1][i][1] * divine_budget_config['zxg']['condition1'][0])
            current_value.append('统计时间内共计添加自选股次数为 ' + str(sql_result[1][i][1]) + ' 次 ' + divine_budget_config['zxg']['condition1'][1])
            temp_value.append(current_value)
    #处理自选股指定时间内取消统计，需开发记录取消时间后才可添加

#神力值功能主流程
def divine_budget_main():
    date_time = set_date_time()
    if date_time != 0:

        db_link = mysql_handle('192.168.10.230', 3306, 'stocksir', 'stocksir1704!')
        db_link.mysql_connect()

        if db_link.status == 1:
            db_link.mysql_select_db('stocksir')

            #股机神力值处理
            add_gj(db_link, date_time)
            #擒牛决神力值处理
            add_qnj(db_link, date_time)
            #股池神力值处理
            add_gc(db_link, date_time)
            #锦囊神力值处理
            add_jn(db_link, date_time)
            #自选股神力值处理
            add_zxg(db_link, date_time)

            db_link.mysql_close_db()

        db_link = mysql_handle('192.168.10.210', 3306, 'root', '123456!@#')
        db_link.mysql_connect()

        if db_link.status == 1:
            db_link.mysql_select_db('agency')

            #第三方神力值处理
            #add_sf(db_link, date_time)

            db_link.mysql_close_db()

        if len(temp_value) != 0:
            #所有股票唯一存放stock_list
            stock_temp_list = []
            for i in range(0,len(temp_value)):
                stock_temp_list.append(temp_value[i][0])
            stock_list = list(set(stock_temp_list))

            #记录合并保存
            #保存记录的模型建立
            calculate_list = []
            for i in range(0,len(stock_list)):
                temp_list = []
                temp_list.append(stock_list[i])
                temp_list.append(0)
                temp_list.append([])
                calculate_list.append(temp_list)
            #记录更新到模型中
            for i in range(0,len(temp_value)):
                #当前记录再模型中的位置，即list中的位置,temp_value与calculate_list的位置是一致的
                num = stock_list.index(temp_value[i][0])
                #神力值累加
                calculate_list[num][1] += temp_value[i][1]
                #神力值累计明细保存
                calculate_list[num][2].append(temp_value[i][2])
            #按神力值记录排序
            array_sec_sort(calculate_list,1)

            #报告文件生成
            html_str_begin = '<html><style> li{font-size:9px} td{vertical-align:middle;text-align:center} td li{text-align:left} .trtitle {font-size:20px;background-color:#FFFF00}</style><head><meta http-equiv="Content-type" content="text/html; charset=utf-8" /><title>结果记录</title></head><body><table border=1px align=center>'
            html_str_middle = '<tr><td colspan=4>从 ' + date_time[0] + ' 至 ' + date_time[1] + ' 神力值统计记录</td></tr><tr class=trtitle><td>序号</td><td>股票代码</td><td>神力值</td><td>神力值累计明细</td></tr>'
            html_str_end = '</table></body></html>'
            '''
            for i in range(0,len(calculate_list)):
                html_str_middle += '<tr>'
                html_str_middle += '<td>' + calculate_list[i][0] + '</td>'
                html_str_middle += '<td>' + str(calculate_list[i][1]) + '</td>'
                html_str_middle += '<td>'
                for j in range(0,len(calculate_list[i][2])):
                    html_str_middle += '<li>' + calculate_list[i][2][j] + '</li>'
                html_str_middle += '</td></tr>'
            html_str = html_str_begin + html_str_middle + html_str_end
            '''
            html_str_middle += set_table_value(calculate_list, 1)
            html_str = html_str_begin + html_str_middle + html_str_end

            fp = open(r"C:\Users\Administrator\Desktop\report.html", 'w')
            fp.write(html_str)
            fp.close()

        else:
            print '无满足条件股票'.decode('utf-8')
    else:
        print '未成功设置查询时间.退出'.decode('utf-8')