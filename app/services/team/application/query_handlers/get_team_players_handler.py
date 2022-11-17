from app.services.team.domain.repository.team import TeamRepositoryInterface
from app.services.team.domain.query.query_interface import QueryInterface

class QueryTeamPlayersHandler():

    def __init__(self, repository: TeamRepositoryInterface, query: QueryInterface, team_name: str = None, players: bool = 0) -> None:
        self.team_name = team_name
        self.repository = repository
        self.players = players
        self.query = query

    def handler(self):
        r = self.query.handler(repository=self.repository, team_name = self.team_name, players = self.players)
        return r
        
        
        
        
