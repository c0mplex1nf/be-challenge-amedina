import requests
import uuid
from app.shared.domain.models.league import Team
from app.services.team.domain.events.team_created import TeamCreated
from app.shared.domain.queue_interface import QueueClientInterface
from app.services.team.domain.commands.command_interface import CommandInterface
from app.services.team.domain.events.team_event_bus_interface import TeamEventBusInterface
from app.services.team.domain.repository.team import TeamRepositoryInterface

class CreateTeamHandler():

    def __init__(self, league: str, code: str, command: CommandInterface, repository: TeamRepositoryInterface, event_bus: TeamEventBusInterface, player_queue: QueueClientInterface) -> None:
        self.code = code
        self.league = league
        self.uri = 'https://api.football-data.org/v4'
        self.bus = event_bus
        self.repository = repository
        self.command = command
        self.player_queue = player_queue

    def handler(self):
        uri = self.uri + f'/competitions/{self.code}/teams'
        headers = {'X-Auth-Token': '2ce15cc075fb491db6c7da4400ba593b'}
        team_data = requests.get(uri, headers=headers).json()
        teams = []
        players = []
        coaches = []
        coach = None

        for team in team_data['teams']:
            id = str(uuid.uuid4())
            teams.append(Team(id=id, league_id=self.league, name=team['name'], short_name=team['shortName'], area_name=team['area']['name'], tla=team['tla'], address=team['address']))

            if not team['squad']:
                coach = team['coach']
                coach['teamId'] = id
                coaches.append(coach)
            
            for player in team['squad']:
                player['teamId'] = id
                players.append(player)

        
        self.command.handler(repository=self.repository, team=teams)

        event = TeamCreated(func_name=self.player_queue.send_message, data={'coach': coaches, 'players': players}) 
        self.bus.add_listener(event)
        self.bus.emit(event)
        self.bus.remove_listener(event)
        
        
        
