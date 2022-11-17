from app.services.player.domain.repository.player import PlayerRepositoryInterface
from app.services.team.domain.commands.command_interface import CommandInterface

class CreatePlayer(CommandInterface):

    def handler(self, repository: PlayerRepositoryInterface, players: list):
        try:
            repository.add(players=players)
        except Exception:
            raise

        