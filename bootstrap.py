import asyncio
import os
from fastapi import FastAPI
from aio_pika import logger
from dotenv import load_dotenv
from config import database
from app.services.league.presentation.controllers.league import LeagueController
from app.services.team.presentation.controllers.team import TeamController
from app.shared.infraestructure.team_queue_client import TeamQueueClient
from app.shared.infraestructure.player_queue_client import PlayerQueueClient



class Bootstrap(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.metadata = database.start_mappers()
        self.league = LeagueController()
        self.team = TeamController()
        self.team_queue_client = TeamQueueClient()
        self.player_queue_client = PlayerQueueClient()
 
app = Bootstrap()
app.include_router(app.league.router, prefix="/league")
app.include_router(app.team.router, prefix="/team")

@app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task_team = loop.create_task(app.team_queue_client.consume(loop=loop))
    task_player = loop.create_task(app.player_queue_client.consume(loop=loop))
    await task_team
    await task_player
