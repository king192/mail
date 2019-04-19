#!/usr/bin/env python
import pika
import time
import sys

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

print(' [*] Waiting for messages. To exit press CTRL+C')


channel.queue_declare(queue='tttt', durable=False)

message = ' '.join(sys.argv[1:]) or '{"mailto":"test@test.com","subject":"I am a queue","content":"Hello World!111111111111111","time":1555663754,"num":166}'
channel.basic_publish(
    exchange='',
    routing_key='tttt',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()
