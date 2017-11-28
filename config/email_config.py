#coding:utf-8

email_config = {
    #发件人
    "sender" : 'liuxu@guxiansheng.cn',
    #收件人,多个收件人按;隔开
    "receiver" : 'ste@guxiansheng.cn',
    #邮件发送服务器
    "smtpserver" : 'smtp.ym.163.com',
    #发件人账号
    "username" : 'liuxu@guxiansheng.cn',
    #发件人密码
    "password" : '123456',
    #邮件标题
    "mail_title" : '自动化测试报告',
    #邮件内容
    "mail_body" : '测试一下邮件到达情况',
    #附件,list
    "attachment": ['HTMLReport.html',r'F:\work\aaaa\test.txt']
}