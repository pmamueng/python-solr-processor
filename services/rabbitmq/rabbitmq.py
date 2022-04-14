import pika


class RabbitMq:

    def __init__(self, message):
        self.message = message

    def send(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=self.message)
        print(f' [x] Sent %s' % self.message)

        connection.close()
