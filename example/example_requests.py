from public.common.common import *
from public.requests_handle import *

method = 'post'
url = r'https://login.api.guxiansheng.cn/index.php?c=user&a=login'
body = r'username=18511903584&password=' + get_md5('654321')
headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
    }

aaa = requests_handle(method, url, body, headers)
result_str = aaa.exc_requests()

bbb = str_to_json(result_str)
print bbb

ccc = dict_filter_columns(bbb,['data','code','message'])
print ccc

if ccc is not False:
    if ccc['code'] == 1:
        print dict_filter_columns(ccc['data'])
    else:
        logging.info(ccc['message'])
