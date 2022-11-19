from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.index import get_shortest_path

app = FastAPI()

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


@app.get('/api/route')
def get_route() -> dict:
    start = (60.184136, 24.949670)
    end = (60.186760, 24.978402)
    route = get_shortest_path(start, end)
    return {'route': route}


# @app.post('/api/route')
# def get_route() -> dict:
