# mail
中间件：rabbitmq-server
```
git clone https://github.com/king192/mail.git
cd mail
cp mail.conf.example mail.conf
#测试邮件发送
python test.py
//消费监听
python consumer.py

另一个终端：
python publish.py
```
