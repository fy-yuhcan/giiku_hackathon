from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from models import User, Food, Recipe, RecipeFood, Storage
from schemas import RecipeCreate, RecipeModel

# レシピを追加
async def add_recipe(session: AsyncSession, recipe: RecipeCreate) -> RecipeModel:
    query = text(
        "INSERT INTO recipes (user_id, title, content) " +
        "VALUES (:user_id, :title, :content) RETURNING id"
    )
    result = await session.execute(query, {"user_id": recipe.user_id, "title": recipe.title, "content": recipe.content})
    recipe_id = result.scalar_one()
    await session.commit()

    return RecipeModel(id=recipe_id, user_id=recipe.user_id, title=recipe.title, content=recipe.content)

# user_idからすべてのレシピを取得
async def get_recipes(session: AsyncSession, user_id: int, num_recipe: int):
    query = text(
        "SELECT * " +
        "FROM recipes " +
        "WHERE user_id = :user_id " +
        "LIMIT :num_recipe"
    )
    result = await session.execute(query, {"user_id": user_id, "num_recipe": num_recipe})
    recipes = result.fetchall()

    return recipes

# recipe_idのレシピを1つ削除
async def delete_recipe(session: AsyncSession, recipe_id: int) -> bool:
    query = text(
        "DELETE FROM recipes " +
        "WHERE id = :recipe_id RETURNING id"
    )
    result = await session.execute(query, {"recipe_id": recipe_id})
    deleted_id = result.scalar()
    await session.commit()

    return deleted_id is not None
