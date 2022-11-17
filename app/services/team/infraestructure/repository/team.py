from fastapi import Depends
from sqlalchemy import insert
from app.services.team.domain.repository.team import TeamRepositoryInterface
from app.shared.domain.models.team import Team
from app.shared.domain.models.player import Player
from config.database import get_session

class TeamSqlAlchemyRepository(TeamRepositoryInterface):

    def __init__(self, session = Depends(get_session)):
        self.session = session

    def add(self, team: list):
        self.session.bulk_save_objects(team)
        self.session.commit()

    def get_team(self, team_name: str = None, players: bool = 0):
        r = self.session.query(Team)

        if not players:
            r = self.session.query( Team.id, Team.name, Team.short_name, Team.tla, Team.address, Team.league_id)

        r = r.filter(Team.name == team_name)

        return r.all()