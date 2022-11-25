from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from index import get_shortest_path

app = FastAPI()


class RoutePoints(BaseModel):
    start: list
    end: list


class Route(BaseModel):
    route: list


origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post('/api/route')
def find_route(route_params: RoutePoints) -> Route:
    print(f'got params {route_params}')
    route = get_shortest_path(route_params.start, route_params.end)
    return {'route': route}
