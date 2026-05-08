import json
import pika
import os


def publish_user_created_event(user_data):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST", "rabbitmq")
        )
    )

    channel = connection.channel()
    channel.exchange_declare(
        exchange="user.exchange",
        exchange_type="topic"
    )

    channel.basic_publish(
        exchange="user.exchange",
        routing_key="user.created",
        body=json.dumps(user_data)
    )

    print("EVENT SENT:", user_data)
    connection.close()
