from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Player:
    id: str
    name: str
    position: str
    birth_date: str
    nationality: str
    type: str
    team_id: str
