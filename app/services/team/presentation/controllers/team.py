import json
from fastapi import APIRouter, Depends, Request
from app.services.team.presentation.controllers.controller import Controller
from app.services.team.application.query_handlers.get_team_players_handler import QueryTeamPlayersHandler
from app.services.team.infraestructure.repository.team import TeamSqlAlchemyRepository
from app.services.team.domain.query.query_players import QueryPlayersByTeam

class TeamController(Controller):

    router = APIRouter()

    def __init__(self) -> None:
        super().__init__()


    @router.get('/players/{team_name}')
    async def list_players(team_name: str = 'PSV' , players: bool = 0, repository =  Depends(TeamSqlAlchemyRepository), query = Depends(QueryPlayersByTeam)):
        response = {}
        query_handler = QueryTeamPlayersHandler(repository=repository, query=query, team_name=team_name, players=players)
        query_response = query_handler.handler()
        response['body'] = query_response
        return response

        
