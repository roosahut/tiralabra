
from invoke import task


@task
def start(ctx):
    ctx.run("python3 backend/src/main.py", pty=True)


def test(ctx):
    ctx.run('pytest backend/src', pty=True)


def coverage(ctx):
    ctx.run('coverage run --branch -m pytest backend/src', pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def lint(ctx):
    ctx.run("pylint backend/src", pty=True)
