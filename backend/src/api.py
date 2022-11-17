from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.index import route_in_lonlat

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
    return {'route': route_in_lonlat}
