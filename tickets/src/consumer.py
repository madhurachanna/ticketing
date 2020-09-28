from src.config import Config
import pika

print("Initializing Pika", flush=True)

URL = Config.BROKER
print(URL)
connection = pika.BlockingConnection(pika.URLParameters(URL))
channel = connection.channel()
channel.queue_declare(queue="hello")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body, flush=True)


channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C", flush=True)

channel.start_consuming()
