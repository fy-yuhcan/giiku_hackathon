from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import *
from sqlalchemy.ext.asynccio import AsyncSession
from sqlalchemy import text
from fastapi import HTTPException
from ..database import Base

#from schemas import 
from ..models import User, Food, Recipe, RecipeFood, Fridge

async def add_food(session: AsyncSession, name: str, unit: str) -> User:
    query = text(
        "INSERT INTO foods" +
        "(name, unit) " +
        "VALUES " +
        "(:name, :unit)"
    )

    result = await session.execute(query, {"name": name, "unit": unit})
    await session.commit()
    return result.fetchone()