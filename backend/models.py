from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, Date, Time, DateTime
from sqlalchemy.orm import relationship

from database import Base

# ここでデータベースのテーブル定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_Key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_Key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_Key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(String, nullable=False)


class RecipeFood(Base):
    __tablename__ = "recipe_foods"
    id = Column(Integer, primary_Key=True)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    


class Fridge(Base):
    __tablename__ = "fridges"
    id = Column(Integer, primary_Key=True)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    added_at = Column(DateTime, nullable=False)
    quantity = Column(Float, nullable=False)