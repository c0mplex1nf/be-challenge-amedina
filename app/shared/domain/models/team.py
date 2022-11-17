from dataclasses import dataclass, field
from typing import List
from app.shared.domain.models.player import Player

@dataclass(unsafe_hash=True)
class Team:
    id: str 
    name: str
    tla: str
    short_name: str
    area_name: str
    address: str
    league_id: str
    players: List[Player] = field(default_factory=list)
