from abc import ABC
from app.shared.domain.models.league import League

class LeagueEventBusInterface(ABC):

  def add_listener(self, event_name, listener):
    raise NotImplemented()


  def remove_listener(self, event_name, listener):
    raise NotImplemented()

  def emit(self, event_name, event):
    raise NotImplemented()

    