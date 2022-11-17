from fastapi import Depends
from sqlalchemy import insert
from app.services.league.domain.repository.league import LeagueRepositoryInterface
from app.shared.domain.models.league import League
from app.shared.domain.models.team import Team
from app.shared.domain.models.player import Player
from app.shared.domain.models.log import Log
from config.database import get_session

class LeagueSqlAlchemyRepository(LeagueRepositoryInterface):

    def __init__(self, session = Depends(get_session)):
        self.session = session

    def add(self, league: League):
        self.session.add(league)
        self.session.commit()

    def add_log(self, log: Log):
        self.session.add(log)
        self.session.commit()

    def log_count(self, code: str):
        r = self.session.query(Log).filter_by(league_code = code).count()
        return r

    def get_last_log(self):
        r = self.session.query(Log).order_by(Log.created_at.desc()).first()
        return r

    def get_league_players(self, league_code = 'CL', filter_name = None):
        
        r = self.session.query(Player).join(League.teams).join(Team.players).filter(League.code == league_code)

        if filter_name:
            r = self.session.query(Player).join(League.teams).join(Team.players).filter(League.code == league_code, Team.name == filter_name)
        
        
        return r.all()