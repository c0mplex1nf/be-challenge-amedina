from app.services.team.domain.repository.team import TeamRepositoryInterface
from app.services.team.domain.commands.command_interface import CommandInterface

class CreateTeam(CommandInterface):

    def handler(self, repository: TeamRepositoryInterface, team: list):
        try:
            repository.add(team=team)
        except Exception:
            raise

        