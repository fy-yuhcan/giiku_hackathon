from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import *
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi import HTTPException

#from schemas import 
from ..models import User, Food, Recipe, RecipeFood, Storage

# レシピに一つの食材を追加
async def add_recipe_foods(session: AsyncSession, food_id: int, recipe_id: int, quantity: int):
    query = text(
        "INSERT INTO recipe_foods" +
        "(food_id, recipe_id, quantity) " +
        "VALUES " +
        "(:food_id, :recipe_id, :quantity)"
    )
    await session.execute(query, {"food_id": food_id, "recipe_id": recipe_id, "quantity": quantity})
    await session.commit()

# recipe_idからそのレシピで使う全ての食材を取得
async def get_recipe_foods(session: AsyncSession, recipe_id: int):
    query = text(
        "SELECT rf.food_id, f.name, f.unit, rf.quantity " +
        "FROM recipe_foods AS rf " +
        "LEFT JOIN foods AS f " +
        "ON rf.food_id = f.id " +
        "WHERE rf.recipe_id = :recipe_id"
    )
    await session.execute(query, {"recipe_id": recipe_id})
    await session.commit()