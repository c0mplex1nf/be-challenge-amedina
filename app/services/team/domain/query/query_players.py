from app.services.team.domain.repository.team import TeamRepositoryInterface
from app.services.team.domain.commands.command_interface import CommandInterface

class QueryPlayersByTeam(CommandInterface):

    def handler(self, repository: TeamRepositoryInterface, team_name: str = None, players: bool = 0):
        try:
            r = repository.get_team(team_name=team_name, players=players)
            return r
        except Exception:
            raise
