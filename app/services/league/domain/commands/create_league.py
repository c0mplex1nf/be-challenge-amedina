from app.services.league.domain.repository.league import LeagueRepositoryInterface
from app.services.league.domain.commands.command_interface import CommandInterface
from app.shared.domain.models.league import League
from app.shared.domain.models.log import Log

class CreateLeague(CommandInterface):

    def handler(self, repository: LeagueRepositoryInterface, league: League, log: Log):
        try:
            repository.add(league)
            repository.add_log(log=log)
        except Exception:
            raise

        