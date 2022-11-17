import pika
import os
import json
import uuid
import logging
import asyncio
import aio_pika
import ast
from aio_pika import logger, connect_robust
from fastapi import Depends
from app.shared.domain.queue_interface import QueueClientInterface
from app.services.team.domain.commands.create_team import CreateTeam
from app.shared.infraestructure.event_bus import EventBus
from app.services.team.infraestructure.repository.team import TeamSqlAlchemyRepository
from app.services.team.application.command_handlers.create_team_handler import CreateTeamHandler
from app.shared.infraestructure.player_queue_client import PlayerQueueClient
from config.database import get_session

class TeamQueueClient(QueueClientInterface):

    def __init__(self):
        self.queue_name = os.environ.get('TEAM_QUEUE', 'team-queue')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=os.environ.get('RABBIT_HOST', 'rabbitmq'), heartbeat=0)
        )
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue=self.queue_name)
        self.callback_queue = self.queue.method.queue
        self.response = None
        logger.info('connection initialized')

    async def consume(self, loop):
        connection = await connect_robust(host=os.environ.get('RABBIT_HOST', 'rabbitmq'), port=5672, loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue(self.queue_name)
        await queue.consume(self.process_incoming_message, no_ack=False)
        logger.info('Established pika async listener')
        return connection

    async def process_incoming_message(self, message):
        await message.ack()
        body = message.body.decode("UTF-8")
        data = ast.literal_eval(body)
        logger.info('Received message')
        if data:
            session = get_session()
            team_handler = CreateTeamHandler(league=data['league_id'],code = data['code'], command=CreateTeam(), 
                repository=TeamSqlAlchemyRepository(session=session), event_bus=EventBus(), 
                player_queue=PlayerQueueClient())
            
            team_handler.handler()


    async def send_message(self, message: dict):

        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )
