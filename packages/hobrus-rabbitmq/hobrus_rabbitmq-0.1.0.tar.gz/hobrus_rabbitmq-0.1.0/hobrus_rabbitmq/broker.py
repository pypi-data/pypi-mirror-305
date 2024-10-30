import os
from faststream import FastStream
from faststream.rabbit import RabbitBroker

RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', '5672')
RABBITMQ_PROTOCOL = os.getenv('RABBITMQ_PROTOCOL', 'amqp')

RABBITMQ_URL = f"{RABBITMQ_PROTOCOL}://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"

broker = RabbitBroker(RABBITMQ_URL)
app = FastStream(broker)