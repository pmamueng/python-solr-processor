import pika

body = "hello_world_2"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=body)
print(f' [x] Sent %s' % body)

connection.close()
