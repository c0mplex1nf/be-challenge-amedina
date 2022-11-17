import json
from fastapi import APIRouter, Depends, Request
from app.services.league.presentation.controllers.controller import Controller
from app.services.league.application.command_handlers.create_league_handler import CreateLeagueHandler
from app.services.league.application.query_handlers.get_league_players_handler import QueryPlayersLeagueHandler
from app.services.league.domain.commands.create_league import CreateLeague
from app.services.league.infraestructure.repository.league import LeagueSqlAlchemyRepository
from app.shared.infraestructure.event_bus import EventBus
from app.shared.infraestructure.team_queue_client import TeamQueueClient
from app.services.league.domain.query.query_players import QueryPlayersByLeague

class LeagueController(Controller):

    router = APIRouter()

    def __init__(self) -> None:
        super().__init__()

    @router.get('/import/{code}')
    async def import_users(code: str = 'CL', command = Depends(CreateLeague), repository =  Depends(LeagueSqlAlchemyRepository), 
                    event_bus = Depends(EventBus), team_queue = Depends(TeamQueueClient)) -> json:
                    
        response = {'message': 'The League have been saved'}
        handler = CreateLeagueHandler(code=code, command=command, repository=repository, event_bus=event_bus, team_queue=team_queue)
        errors = handler.handler()

        if errors:
            response['message'] = errors

        return response

    @router.get('/players/{league_code}')
    async def list_players(league_code: str = 'CL' , team_name: str = None, repository =  Depends(LeagueSqlAlchemyRepository), query = Depends(QueryPlayersByLeague)):
        response = {}
        query_handler = QueryPlayersLeagueHandler(repository=repository, query=query, league_code=league_code, filter_team=team_name)
        query_response = query_handler.handler()
        response['body'] = query_response
        return response

        
