from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import *
from sqlalchemy.ext.asynccio import AsyncSession
from sqlalchemy import text
from fastapi import HTTPException

#from schemas import 
from ..models import User, Food, Recipe, RecipeFood, Fridge

# レシピを追加
async def add_recipe(session: AsyncSession, user_id: int, title: str, content: str):
    query = text(
        "INSERT INTO recipes" +
        "(user_id, title, content) " +
        "VALUES " +
        "(:user_id, :title, :content)"
    )
    await session.execute(query, {"user_id": user_id, "title": title, "content": content})
    await session.commit()

# user_idからすべてのレシピを取得
async def get_recipes(session: AsyncSession, user_id: int):
    query = text(
        "SELECT * " +
        "FROM recipes " +
        "WHERE user_id = :user_id"
    )
    await session.execute(query, {"user_id": user_id})
    await session.commit()

# recipe_idのレシピを1つ削除
async def delete_recipe(session: AsyncSession, recipe_id: int):
    query = text(
        "DELETE FROM recipes " +
        "WHERE id = :recipe_id"
    )
    await session.execute(query, {"recipe_id": recipe_id})
    await session.commit()