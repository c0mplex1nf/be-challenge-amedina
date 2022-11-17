from app.services.league.domain.repository.league import LeagueRepositoryInterface
from app.services.league.domain.commands.command_interface import CommandInterface

class QueryPlayersByLeague(CommandInterface):

    def handler(self, repository: LeagueRepositoryInterface, filter_team: str = None, league_code: str = 'CL'):
        try:
            r = repository.get_league_players(league_code=league_code, filter_name=filter_team)
            return r
        except Exception:
            raise
