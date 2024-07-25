from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import *
from fastapi import HTTPException
from models import *
from schemas import *

# ここにデータベース操作を書く
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも

def get_recipe(db: Session, user_id: int, num_recipe: int):
    recipes = db.scalars(
        select(RecipeFood)
        .join(Food, RecipeFood.food_id == Food.id)
        .join(Recipe, RecipeFood.recipe_id == Recipe.id)
        .where(Recipe.user_id == user_id)
        .limit(num_recipe)
    ).all()
    if recipes is None:
        return HTTPException(status_code=404, detail="recipes not found")
    return recipes