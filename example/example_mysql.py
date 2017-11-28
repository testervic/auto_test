from public.common.common import *
from public.mysql_handle import *

test = mysql_handle('192.168.10.230', 3306, 'stocksir', 'stocksir1704!')
test.mysql_connect()
if test.status == 1:
    test.mysql_select_db('stocksir')
    sql = 'select * from stock_member where member_mobile = "11111" limit 10'
    result = test.exc_sql(sql)
    test.mysql_close_db()
