from abc import ABC
from app.services.team.domain.repository.team import TeamRepositoryInterface

class QueryInterface(ABC):

    def handler(self, repository: TeamRepositoryInterface, team_name: str = None, players: bool = 0):
        raise NotImplemented()

        