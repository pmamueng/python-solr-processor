import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [X] Waiting for messages.')
channel.start_consuming()
