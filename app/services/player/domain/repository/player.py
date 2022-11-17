from abc import ABC

class PlayerRepositoryInterface(ABC):
    
    def add(self, players: list):
        raise NotImplemented()