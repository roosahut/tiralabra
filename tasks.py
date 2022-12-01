
from invoke import task


@task
def start(ctx):
    ctx.run("python3 backend/src/main.py", pty=True)
