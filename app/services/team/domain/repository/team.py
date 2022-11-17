from abc import ABC

class TeamRepositoryInterface(ABC):
    
    def add(self, team: list):
        raise NotImplemented()

    def get_team(self, team_name: str = None, players: bool = 0):
        raise NotImplemented()