from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import *
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi import HTTPException
from schemas import FoodModel
# from models import Food

# 食材を一つ追加
# async def add_food(session: AsyncSession, name: str, unit: str) -> None:
#     query = text(
#         "INSERT INTO foods" +
#         "(name, unit) " +
#         "VALUES " +
#         "(:name, :unit)"
#     )
#     await session.execute(query, {"name": name, "unit": unit})
#     await session.commit()

# 全ての食材を取得
async def get_foods(session: AsyncSession) -> list[FoodModel]:
    query = text(
        "SELECT * " +
        "FROM foods"
    )
    result = await session.execute(query)
    foods = result.fetchall()
    return foods