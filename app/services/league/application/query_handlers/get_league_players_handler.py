from app.services.league.domain.repository.league import LeagueRepositoryInterface
from app.services.league.domain.query.query_interface import QueryInterface

class QueryPlayersLeagueHandler():

    def __init__(self, repository: LeagueRepositoryInterface, query: QueryInterface, filter_team: str = None, league_code : str = 'CL') -> None:
        self.league_code = league_code
        self.repository = repository
        self.filter_team = filter_team
        self.query = query

    def handler(self):
        r = self.query.handler(repository=self.repository, filter_team=self.filter_team, league_code=self.league_code)
        return r
        
        
        
        
