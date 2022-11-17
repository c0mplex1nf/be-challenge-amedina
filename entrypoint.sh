#!/bin/bash

FILE=league.db

if ! [ -f "$FILE" ]; then
    alembic revision --autogenerate -m "Create Database"
    alembic upgrade head
    uvicorn bootstrap:app --reload --host 0.0.0.0 --port 8000
else
    alembic revision -m "A change ocurred"
    alembic upgrade head
    uvicorn bootstrap:app --reload --host 0.0.0.0 --port 8000
fi


