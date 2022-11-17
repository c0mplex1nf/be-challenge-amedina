from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper
from app.shared.domain.models.team import Team

def createTable(metadata):
    team = Table(
        "team",
        metadata,
        Column("id", String(255), primary_key=True),
        Column("name", String(255), nullable=True),
        Column("tla", String(255), nullable=True),
        Column("short_name", String(255), nullable=True),
        Column("area_name", String(255), nullable=True),
        Column("address", String(255), nullable=True),
        Column('league_id', String(255), ForeignKey('league.id'))
    )
    
    return team