from abc import ABC

class TeamEventBusInterface(ABC):

  def add_listener(self, event_name, listener):
    raise NotImplemented()

  def remove_listener(self, event_name, listener):
    raise NotImplemented()

  def emit(self, event_name, event):
    raise NotImplemented()

    