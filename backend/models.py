from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, DateTime
from sqlalchemy.orm import relationship

from database import Base

# ここでデータベースのテーブル定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)


class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String)


class RecipeFood(Base):
    __tablename__ = "recipe_foods"
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey("foods.id"))
    recipe_id = Column(Integer)
    


class Fridge(Base):
    __tablename__ = "fridges"
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey("foods.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    added_at = Column(DateTime)
    quantity = Column(Integer)