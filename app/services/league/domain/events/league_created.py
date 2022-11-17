from dataclasses import dataclass, field
from typing import List, Callable
from app.shared.domain.models.team import Team
from app.services.league.domain.events.event_interface import EventInterface

@dataclass(unsafe_hash=True)
class LeagueCreated(EventInterface):
    name: str = 'leagued-created'