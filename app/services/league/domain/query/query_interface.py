from abc import ABC
from app.services.league.domain.repository.league import LeagueRepositoryInterface

class QueryInterface(ABC):

    def handler(self, repository: LeagueRepositoryInterface, filter_team: str = None, league_code :str = 'CL'):
        raise NotImplemented()

        