from abc import ABC
from app.shared.domain.models.league import League
from app.shared.domain.models.log import Log

class LeagueRepositoryInterface(ABC):
    
    def add(self, league: League) -> None:
        raise NotImplemented()

    def add_log(self, log: Log) -> None:
        raise NotImplemented()

    def log_count(self, code: str) -> int:
        raise NotImplemented()

    def get_last_log(self):
        raise NotImplemented()

    def get_league_players(self, league_code, filter_name):
        raise NotImplemented()