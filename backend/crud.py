from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import *
from fastapi import HTTPException

#from schemas import 
from models import User, Food, Recipe, RecipeFood, Fridge


# ここにデータベース操作を書く
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも

def get_recipe(db: Session, user_id: int, num_recipe: int):
    data = db.scalars(
    ).all()
    return data


def get_fridge(db: Session, user_id: int):
    data = db.scalars(
    )