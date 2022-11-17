from fastapi import Depends
from app.services.player.domain.repository.player import PlayerRepositoryInterface
from config.database import get_session

class PlayerSqlAlchemyRepository(PlayerRepositoryInterface):

    def __init__(self, session = Depends(get_session)):
        self.session = session

    def add(self, players: list):
        self.session.bulk_save_objects(players)
        self.session.commit()