import asyncio
from app.services.league.domain.events.league_event_bus_interface import LeagueEventBusInterface
from app.services.league.domain.events.event_interface import EventInterface

class EventBus(LeagueEventBusInterface):

  def __init__(self):
    self.listeners = {}

  def add_listener(self, event: EventInterface):
    
    event_name = event.name
    listener = event.func_name

    if not self.listeners.get(event_name, None):
      self.listeners[event_name] = {listener}
    else:
      self.listeners[event_name].add(listener)

  def remove_listener(self, event: EventInterface):
    
    event_name = event.name
    listener = event.func_name

    self.listeners[event_name].remove(listener)
    if len(self.listeners[event_name]) == 0:
      del self.listeners[event_name]

  def emit(self, event: EventInterface):
    event_name = event.name
    data = event.data
    listeners = self.listeners.get(event_name, [])
    for listener in listeners:
      asyncio.create_task(listener(data))