import pickle
from graph.graph import Graph
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from index import get_shortest_path

app = FastAPI()


class RoutePoints(BaseModel):
    start: list
    end: list


class Route(BaseModel):
    fringe: dict
    dijkstra: dict


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

G = pickle.load(open('./backend/data/helsinki_graph.pickle', 'rb'))
graph = Graph(G)


@app.post('/api/route')
def find_route(route_params: RoutePoints) -> Route:
    print(f'got params {route_params}')
    values = get_shortest_path(
        route_params.start, route_params.end, graph, G)
    return values


app.mount('/', StaticFiles(directory='./backend/src/build/',
          html=True), name='root')
