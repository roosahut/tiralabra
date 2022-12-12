import uvicorn


def start():
    """Starts the app using uvicorn
    """
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
