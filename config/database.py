import os
from sqlalchemy import orm, create_engine
from app.shared.infraestructure.migrations.league import createTable as createLeagueTable
from app.shared.infraestructure.migrations.team import createTable as createTeamTable
from app.shared.infraestructure.migrations.player import createTable as createPlayerTable
from app.shared.infraestructure.migrations.log import createTable as createLogTable
from app.shared.domain.models.player import Player
from app.shared.domain.models.team import Team
from app.shared.domain.models.league import League
from app.shared.domain.models.log import Log


registry  = orm.registry()

def start_mappers():
    db_league = createLeagueTable(registry.metadata)
    db_team = createTeamTable(registry.metadata)
    db_player = createPlayerTable(registry.metadata)
    db_log = createLogTable(registry.metadata)

    registry.map_imperatively(League, db_league, properties={
        'teams' : orm.relationship(Team, backref='league', order_by=db_team.c.id)
    })

    registry.map_imperatively(Team, db_team, properties={
        'players' : orm.relationship(Player, backref='team', order_by=db_player.c.id)
    })

    registry.map_imperatively(Player, db_player)
    registry.map_imperatively(Log, db_log)

    return registry.metadata

def get_session():
    engine = create_engine(os.environ.get("DATABASE_URL"))
    session = orm.sessionmaker(bind=engine)
    return session()