import pika
import sys
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='benchmark', durable=True)

loop = int(sys.argv[1]) or 10
for i in range(loop):
    message = str(uuid.uuid4())
    channel.basic_publish(exchange='',
                          routing_key='benchmark',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode = 2, # make message persistent
                          ))
    print(' [x] Sent {}'.format(message))
connection.close()
