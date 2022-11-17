import pika
import os
import json
import uuid
import logging
import asyncio
import aio_pika
from aio_pika import logger, connect_robust
from app.shared.domain.queue_interface import QueueClientInterface

class QueueClient(QueueClientInterface):

    def __init__(self, process_callable, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=os.environ.get('RABBIT_HOST', 'rabbitmq'), heartbeat=0)
        )
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue=self.queue_name)
        self.callback_queue = self.queue.method.queue
        self.response = None
        self.process_callable = process_callable
        logger.info('connection initialized')

    async def consume(self, loop):
        """Setup message listener with the current running loop"""
        connection = await connect_robust(host=os.environ.get('RABBIT_HOST', 'rabbitmq'), port=5672, loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue(self.queue_name)
        await queue.consume(self.process_incoming_message, no_ack=False)
        logger.info('Established pika async listener')
        return connection

    async def process_incoming_message(self, message):
        """Processing incoming message from RabbitMQ"""
        await message.ack()
        body = message.body
        logger.info('Received message')
        if body:
            self.process_callable(json.loads(body))

    def send_message(self, message: dict):
        """Method to publish message to RabbitMQ"""
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )
