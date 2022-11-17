from dataclasses import dataclass, field
from typing import List, Callable
from app.shared.domain.models.team import Team
from abc import ABC

@dataclass(unsafe_hash=True)
class EventInterface(ABC):
    func_name: Callable
    data: str
    name: str