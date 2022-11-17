from abc import ABC
from app.services.player.domain.repository.player import PlayerRepositoryInterface

class CommandInterface(ABC):

    def handler(self, repository: PlayerRepositoryInterface, players: list):
        raise NotImplemented()

        