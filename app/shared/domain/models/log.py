from dataclasses import dataclass, field
from typing import List
from app.shared.domain.models.team import Team
from datetime import datetime

@dataclass(unsafe_hash=True)
class Log:
    id: str
    league_code: str
    created_at: datetime = field(default_factory=datetime.now)
