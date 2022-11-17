from abc import ABC
from app.services.team.domain.repository.team import TeamRepositoryInterface

class CommandInterface(ABC):

    def handler(self, repository: TeamRepositoryInterface, team: list):
        raise NotImplemented()

        