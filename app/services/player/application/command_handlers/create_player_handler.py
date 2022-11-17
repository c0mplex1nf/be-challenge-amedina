import requests
import uuid
from app.shared.domain.models.player import Player
from app.shared.domain.queue_interface import QueueClientInterface
from app.services.player.domain.commands.command_interface import CommandInterface
from app.services.player.domain.repository.player import PlayerRepositoryInterface

class CreatePlayerHandler():

    def __init__(self, players: list, coach: dict, command: CommandInterface, repository: PlayerRepositoryInterface) -> None:
        self.repository = repository
        self.command = command
        self.players = players
        self.coaches = coach

    def handler(self):
        players = []
        
        for player in self.players:
            id = str(uuid.uuid4())
            players.append(Player(id=id, team_id=player['teamId'], name=player['name'], position=player['position'], birth_date=player['dateOfBirth'], nationality=player['nationality'], type='player'))

        for coach in self.coaches:
            id = str(uuid.uuid4())
            players.append(Player(id=id, team_id=coach['teamId'], name=coach['name'], position=None, birth_date=coach['dateOfBirth'], nationality=coach['nationality'], type='coach'))

        self.command.handler(repository=self.repository, players=players)

        
        
        
