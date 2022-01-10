from app.db import tires, database
from app.serializers import TireIn


async def add_tire(data_in: TireIn):
    query = tires.insert().values(**data_in.dict())
    return await database.execute(query=query)


async def get_tires():
    query = tires.select()
    return await database.fetch_all(query=query)
