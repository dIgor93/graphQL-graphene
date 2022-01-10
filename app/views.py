from fastapi import APIRouter

from app.db_manager import add_tire, get_tires
from app.serializers import TireIn


router = APIRouter()


@router.post("/add")
async def add(payload: TireIn):
    id = await add_tire(payload)
    return {"RecordId": id}


@router.get("/get_all")
async def get_all():
    return await get_tires()
