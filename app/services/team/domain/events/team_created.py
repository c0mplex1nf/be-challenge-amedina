from dataclasses import dataclass, field
from app.services.team.domain.events.event_interface import EventInterface

@dataclass(unsafe_hash=True)
class TeamCreated(EventInterface):
    name: str = 'team-created'