import requests
import uuid
import os
from datetime import datetime
from app.shared.domain.models.league import League
from app.shared.domain.models.log import Log
from app.services.league.domain.events.league_created import LeagueCreated
from app.shared.domain.queue_interface import QueueClientInterface
from app.services.league.domain.commands.command_interface import CommandInterface
from app.services.league.domain.events.league_event_bus_interface import LeagueEventBusInterface
from app.services.league.domain.repository.league import LeagueRepositoryInterface

class CreateLeagueHandler():

    def __init__(self, code: str, command: CommandInterface, repository: LeagueRepositoryInterface, event_bus: LeagueEventBusInterface, team_queue: QueueClientInterface) -> None:
        self.code = code
        self.uri = 'https://api.football-data.org/v4'
        self.bus = event_bus
        self.repository = repository
        self.command = command
        self.team_queue = team_queue

    def handler(self):
        now = datetime.now()
        uri = self.uri + f'/competitions/{self.code}'
        headers = {'X-Auth-Token': os.environ.get('AUTH_TOKEN')}
        log_count = self.repository.log_count(self.code)
        last_log = self.repository.get_last_log()
        seconds_difference = 100000
        
        if last_log:
            seconds_difference = (now-last_log.created_at).total_seconds()

        if seconds_difference < 30:
            return 'You reach the max amount of requests pleas wait at least 30 seconds for the next import'
    
        if log_count:
            return 'This leagues was already imported'

        league_data = requests.get(uri, headers=headers).json()
        
        if 'message' in league_data:
            return league_data['message']

        if not league_data:
            return 'Probably the league code you send does not exist'

        id = str(uuid.uuid4())
        log_id = str(uuid.uuid4())
        league = League(id=id, name=league_data['name'], area_name=league_data['area']['name'], code=self.code)
        log = Log(id=log_id, league_code=self.code)
        self.command.handler(league=league, repository=self.repository, log=log)

        event = LeagueCreated(func_name=self.team_queue.send_message, data={'league_id':id, 'code': self.code}) 
        self.bus.add_listener(event)
        self.bus.emit(event)
        self.bus.remove_listener(event)
        
        
        
