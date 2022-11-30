import uvicorn


def start():
    uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=True)
