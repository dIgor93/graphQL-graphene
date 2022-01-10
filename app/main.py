from fastapi import FastAPI

from app.db import metadata, engine, database
from app.views import router

metadata.create_all(engine)


app = FastAPI()


@app.on_event('startup')
async def start():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(router)
