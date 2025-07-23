from fastapi import FastAPI

from api.routes import devops

app = FastAPI()

app.include_router(devops.router, tags=["devops"])
