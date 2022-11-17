from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper
from app.shared.domain.models.player import Player

def createTable(metadata):
    player = Table(
        "player",
        metadata,
        Column("id", String(255), primary_key=True, nullable=True),
        Column("name", String(255), nullable=True),
        Column("position", String(255), nullable=True),
        Column("birth_date", String(255), nullable=True),
        Column("nationality", String(255), nullable=True),
        Column("type", String(255), nullable=True),
        Column('team_id', String(255), ForeignKey('team.id'))
    )
    
    return player