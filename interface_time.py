#coding:utf-8
from public.common.common import *
from public.requests_handle import *
import random
import datetime
from example.example_threading import *

#前面补充指定数量的单个字符
def str_fill_tag(str, num, single_tag):
    if len(str) < num:
        temp_str = ''
        for i in range(0, (num-len(str))):
            temp_str += single_tag
        return single_tag + str
    else:
        return str

#datetime时间转字典
def dict_time(time):
    time_config = {
        'h' : 0,
        'm' : 0,
        's' : 0,
        'ms' : 0
    }
    temp_time = str(time)
    temp_time = temp_time.split('.')
    time_config['ms'] = temp_time[1]
    temp_time[0] = temp_time[0].split(':')
    time_config['h'] = temp_time[0][0]
    time_config['m'] = temp_time[0][1]
    time_config['s'] = temp_time[0][2]
    return  time_config

#时间转为毫秒级时间数据
def time_to_mstime(dict_time):
    if len(dict_time['h']) <= 2:
        mstime = long(dict_time['ms'])
        mstime += long(dict_time['s']) * 1000000
        mstime += long(dict_time['m']) * 1000000 * 60
        mstime += long(dict_time['h']) * 1000000 * 60 * 60
        return mstime
    else:
        print '累计时间可能大于1天'.decode('utf-8')
        return False

#平均时间处理
def avg_time(mstime, num):
    if isinstance(mstime, (int, long)) and isinstance(num, int):
        result_time = {
            'h' : 0,
            'm' : 0,
            's' : 0,
            'ms' : 0
        }
        if num <= 0:
            print '次数应该为大于0的整数'.decode('utf-8')
            return False
        else:
            avg_mstime = mstime / num
            result_time['ms'] = avg_mstime % 1000000
            result_time['s'] = avg_mstime / 1000000 % 60
            result_time['m'] = avg_mstime / (1000000 * 60) % 60
            result_time['h'] = avg_mstime / (1000000 * 60 * 60)
            return str(result_time['h']) + ':' + str_fill_tag(str(result_time['m']),2,'0') + ':' + str_fill_tag(str(result_time['s']),2,'0') + '.' + str_fill_tag(str(result_time['ms']),6,'0')
    else:
        print '时间和次数均应为整数'.decode('utf-8')
        return False

def interface_time(num, mobile_init, username_init):
    num = num
    pre_name = ['琪琪', '娟娟', '慧慧', '灰灰', '兰兰', '琳琳', '围围', '首成', '小冶冶', '强强']
    middle_name = '的'
    end_name = ['小情人', '小乖乖', '姐姐', '妹妹', '小星星', '小弟弟', '大姨妈', '萌萌']
    end_name += pre_name
    mobile_init = mobile_init
    username_init = username_init
    requests_h = requests_handle()
    #成功次数
    success_num = 0
    #失败次数
    fail_num = 0
    #接口错误次数
    error_num = 0
    #整体接口消耗时间
    total_elapsed_time = 0
    #平均消耗时间
    avg_elapsed_time = 0
    #最大消耗时间
    max_elapsed_time = 0
    #最小消耗时间
    min_elapsed_time = 0

    for i in range (0, num):
        username = username_init + str(i)
        password = '123456'
        mobile = mobile_init + i
        nickname = random.choice(pre_name) + middle_name + random.choice(end_name)

        method = 'post'
        url = r'http://crm.guxiansheng.cn/admin/user/addUser'
        body = {
            'username' : username,
            'password' : password,
            'mobile' : mobile,
            'nickname' : nickname
        }
        headers = {
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": r"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
                "Cookie": r"admin=%7B%22id%22%3A1%2C%22username%22%3A%22admin%22%2C%22nickname%22%3A%22%5Cu4e09%5Cu946badmin11%22%2C%22avatar%22%3A%22http%3A%5C%2F%5C%2Fgxscrm-static.oss-cn-shenzhen.aliyuncs.com%5C%2Fassets%5C%2Fimg%5C%2Favatar.png%22%2C%22mobile%22%3A%2213211112223%22%2C%22token%22%3A%2224a92c9e-7240-47f7-a34b-dd988956a98b%22%7D; keeplogin=%221%7C2592000%7C1512503039%7C5fc68aa48b99e092743cf79a80da2339%22; PHPSESSID=77g8qgh67ob6mv7om5bhnj7s16"
            }

        requests_h.set_requests_para(method, url, body, headers)
        begin = datetime.datetime.now()
        result_str = requests_h.exc_requests()
        end = datetime.datetime.now()
        elapsed_time = end - begin
        if i == 0:
            total_elapsed_time = elapsed_time
            max_elapsed_time = elapsed_time
            min_elapsed_time = elapsed_time
        else:
            total_elapsed_time += elapsed_time
            if elapsed_time > max_elapsed_time:
                max_elapsed_time = elapsed_time
            elif elapsed_time < min_elapsed_time:
                min_elapsed_time = elapsed_time
        print '本次消耗时间为 : '  + str(elapsed_time)

        #判断接口插入是否成功
        bbb = str_to_json(result_str)

        ccc = dict_filter_columns(bbb,['data','code','message'])

        if result_str is not False:
            if ccc['code'] == 1:
                success_num += 1
            else:
                fail_num += 1
        else:
            error_num += 1

    #计算平均时间
    avg_elapsed_time = avg_time(time_to_mstime(dict_time(total_elapsed_time)), num)
    '''
    print "总共运行次数 : " + str(num)
    print "成功次数 : " + str(success_num)
    print "失败次数 : " + str(fail_num)
    print "报错次数 : " + str(error_num)
    print "单次请求最长消耗时间为 : " + str(max_elapsed_time)
    print "单次请求最短消耗时间为 : " + str(min_elapsed_time)
    print "全部接口请求消耗时间为 : " + str(total_elapsed_time)
    print "全部接口平均消耗时间为 : " + str(avg_elapsed_time)
    '''
    return_dict = {
            'total_num': num,
            'success_num': success_num,
            'fail_num': fail_num,
            'error_num': error_num,
            'max_elapsed_time': str(max_elapsed_time),
            'min_elapsed_time': str(min_elapsed_time),
            'total_elapsed_time': str(total_elapsed_time),
            'avg_elapsed_time': str(avg_elapsed_time)
    }

    return return_dict


loop_args = ((50, 15100200000, 'bbb'), (50, 15100300000, 'ccc'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'), (50, 15100300000, 'ccc'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'), (50, 15100300000, 'ccc'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'),(50, 15100400000, 'ddd'))

treads = loop_create_func(interface_time, loop_args)
loop_threads_start(treads)
loop_threads_join(treads)
for i in range (0,len(treads)):
    print treads[i].getResult()['avg_elapsed_time']
