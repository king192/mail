#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Mailer import Mailer
from configobj import ConfigObj 
class Send():
    def __init__(self):
        pass
        
    def send(self, subject, content):
        config = ConfigObj("mail.conf",encoding='UTF8')
        mail = Mailer(config['mail.smtp']['addr'], config['mail.smtp']['password'], config['mail.smtp']['smtp'], config['mail.smtp']['port'],'1434970057@qq.com')
        res = mail.mail(subject, content)
        print (res)
