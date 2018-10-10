#!/usr/bin/env python
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='benchmark', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(' [x] Received {}'.format(body))
    time.sleep(body.count(b'.'))
    print(' [x] Done')
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='benchmark')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
