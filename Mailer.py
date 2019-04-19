#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

class Mailer():
    """docstring for Mailer"""
    my_sender=''    # 发件人邮箱账号
    my_smtp = ''
    my_pass = ''              # 发件人邮箱密码
    my_port = ''
    mailto=''      # 收件人邮箱账号，我这边发送给自己
    def __init__(self, my_sender, my_pass, my_smtp, my_port, mailto):
        super(Mailer, self).__init__()
        self.my_sender = my_sender
        self.my_smtp = my_smtp
        self.my_port = my_port
        self.mailto = mailto
        self.my_pass = my_pass

    def mail(self, subject, content):
        ret=True
        try:
            msg=MIMEText('邮件内容:' + content,'plain','utf-8')
            msg['From']=formataddr(["beien",self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["xhq",self.mailto])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']=subject + ":"              # 邮件的主题，也可以说是标题

            server=smtplib.SMTP_SSL(self.my_smtp, self.my_port)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender,[self.mailto,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print (e)
            ret=False
        return ret
