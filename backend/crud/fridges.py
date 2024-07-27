from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models import User, Food, Recipe, RecipeFood, Fridge
# from schemas import FridgeSchema, FoodSchema, RecipeSchema

# 冷蔵庫に食材を追加
async def add_fridge(session: AsyncSession, user_id: int, food_id: int, quantity: float):
    query = text(
        "INSERT INTO fridges (user_id, food_id, quantity, added_at) " +
        "VALUES (:user_id, :food_id, :quantity, current_timestamp)"
    )
    await session.execute(query, {"user_id": user_id, "food_id": food_id, "quantity": quantity})
    await session.commit()

# user_idから冷蔵庫のすべての食材を取得（foodとjoin）
async def get_fridge(session: AsyncSession, user_id: int):
    query = text(
        "SELECT " + 
        "foods.id, foods.name, foods.unit " +
        "SUM(fridges.quantity) AS total_quantity, " + 
        "MIN(fridges.added_at) AS earliest_added_at " +
        "FROM fridges " +
        "LEFT JOIN foods ON fridges.food_id = foods.id " +
        "WHERE fridges.user_id = :user_id " +
        "GROUP BY foods.id, foods.name, foods.unit " +
        "ORDER BY earliest_added_at"
    )
    result = await session.execute(query, {"user_id": user_id})
    fridge_contents = result.fetchall()
    return fridge_contents

# 冷蔵庫の食材の詳細（それぞれの買った日、残っている量）を取得
async def get_fridge_by_food(session: AsyncSession, user_id: int, food_id: int):
    query = text(
        "SELECT " +
        "foods.id, foods.name, foods.unit, fridges.added_at, fridges.quantity " +
        "FROM fridges " +
        "LEFT JOIN foods ON fridges.food_id = foods.id " +
        "WHERE fridges.user_id = :user_id " +
        "AND fridges.food_id = :food_id " +
        "ORDER BY fridges.added_at"
    )
    result = await session.execute(query, {"user_id": user_id, "food_id": food_id})
    fridge_foods = result.fetchall()
    return fridge_foods

# 冷蔵庫の特定の食材を削除
async def remove_fridge(session: AsyncSession, fridge_id: int):
    query = text(
        "DELETE FROM fridges " +
        "WHERE id = :fridge_id"
    )
    await session.execute(query, {"fridge_id": fridge_id})
    await session.commit()

# 冷蔵庫の食材の量を更新（減らす）
async def update_fridge(session: AsyncSession, fridge_id: int, quantity: float):
    query = text(
        "UPDATE fridges " +
        "SET quantity = :quantity " +
        "WHERE id = :fridge_id"
    )
    await session.exeute(query, {"fridge_id": fridge_id, "quantity": quantity})
    await session.commit()

