from Mailer import Mailer
from configobj import ConfigObj 

config = ConfigObj("mail.conf",encoding='UTF8')
mail = Mailer(config['mail.smtp']['addr'], config['mail.smtp']['password'], config['mail.smtp']['smtp'], config['mail.smtp']['port'],'1434970057@qq.com')
res = mail.mail('test mail', 'i am a test mail')
print (res)
