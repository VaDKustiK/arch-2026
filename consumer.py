import pika
import json


def callback(ch, method, properties, body):
    data = json.loads(body)
    print("NOTIFICATION SERVICE RECEIVED EVENT")
    print(data)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel = connection.channel()

channel.exchange_declare(
    exchange="user.exchange",
    exchange_type="topic"
)

channel.queue_declare(queue="user.events")

channel.queue_bind(
    exchange="user.exchange",
    queue="user.events",
    routing_key="user.#"
)

channel.basic_consume(
    queue="user.events",
    on_message_callback=callback,
    auto_ack=True
)

print("waiting for events")
channel.start_consuming()
