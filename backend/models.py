from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, Date, Time, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

from database import Base

# ここでデータベースのテーブル定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    recipes = relationship("Recipe", backref="user")
    storages = relationship("Storage", backref="user")

class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)

    recipe_foods = relationship("RecipeFood", backref="food")
    storages = relationship("Storage", backref="food")

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    recipe_foods = relationship("RecipeFood", backref="recipe")

class RecipeFood(Base):
    __tablename__ = "recipe_foods"
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    quantity = Column(Float, nullable=False)

class Storage(Base):
    __tablename__ = "storages"
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    added_at = Column(Timestamp, server_default=current_timestamp())
    quantity = Column(Float, nullable=False)


