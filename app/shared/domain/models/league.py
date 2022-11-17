from dataclasses import dataclass, field
from typing import List
from app.shared.domain.models.team import Team

@dataclass(unsafe_hash=True)
class League:
    id: str
    name: str
    area_name: str
    code: str
    teams: List[Team] = field(default_factory=list)
