from abc import ABC
from app.services.league.domain.repository.league import LeagueRepositoryInterface
from app.shared.domain.models.league import League
from app.shared.domain.models.log import Log

class CommandInterface(ABC):

    def handler(self, repository: LeagueRepositoryInterface, league: League, log:Log):
        raise NotImplemented()

        