from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models import User, Food, Recipe, RecipeFood, Fridge
from schemas import FridgeCreate, FridgeUpdate, FridgeWithFoodInfo, FoodInFridge

# 冷蔵庫に食材を追加
async def add_fridge(session: AsyncSession, user_id: int, food_id: int, quantity: float):
    query = text(
        "INSERT INTO fridges (user_id, food_id, quantity, added_at) " +
        "VALUES (:user_id, :food_id, :quantity, current_timestamp)"
    )
    await session.execute(query, {"user_id": user_id, "food_id": food_id, "quantity": quantity})
    await session.commit()

# user_idから冷蔵庫のすべての食材を取得（foodとjoin）
async def get_fridge(session: AsyncSession, user_id: int) -> list[FridgeWithFoodInfo]:
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
    fridge_results = result.fetchall()

    fridge = [
        FridgeWithFoodInfo(
            food_id = row[0],
            name = row[1],
            unit = row[2],
            total_quantity = row[3],
            earliest_added_at = row[4]
        )
        for row in fridge_results
    ]
    return fridge

# 冷蔵庫の食材の詳細（それぞれの買った日、残っている量）を取得
async def get_fridge_by_food(session: AsyncSession, user_id: int, food_id: int) -> list[FoodInFridge]:
    query = text(
        "SELECT " +
        "fridges.id AS fridge_id"
        "foods.id AS food_id" + 
        "foods.name, foods.unit, fridges.added_at, fridges.quantity " +
        "FROM fridges " +
        "LEFT JOIN foods ON fridges.food_id = foods.id " +
        "WHERE fridges.user_id = :user_id " +
        "AND fridges.food_id = :food_id " +
        "ORDER BY fridges.added_at"
    )
    result = await session.execute(query, {"user_id": user_id, "food_id": food_id})
    fridge_foods_results = result.fetchall()

    fridge_foods = [
        FoodInFridge(
            fridge_id = row[0],
            food_id = row[1],
            name = row[2],
            unit = row[3],
            added_at = row[4],
            quantity = row[5]
        )
    ]
    return fridge_foods_results

# 冷蔵庫の特定の食材を削除
async def delete_fridge(session: AsyncSession, fridge_id: int):
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

