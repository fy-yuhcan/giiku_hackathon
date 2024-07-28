from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone
from models import User, Food, Recipe, RecipeFood, Storage
from schemas import StorageCreate, StorageUpdate, StorageWithFoodInfo, StorageSummaryWithFoodInfo, FoodInStorage, StorageFood

# 冷蔵庫に食材を複数追加
async def add_storages(session: AsyncSession, storages_create: list[StorageCreate]):
    storages_create_size = len(storages_create)
    value_clause = ", ".join(
        f"(:user_id_{i}, :food_id_{i}, :quantity_{i}, :added_at_{i}, )" for i in range(storages_create_size)
    )

    query = text(
        "INSERT INTO storages (user_id, food_id, quantity, added_at) " +
        "VALUES {value_clause}"
    )

    params = {
        key: value
        for i, storage in enumerate(storages_create)
        for key, value in {
            f"user_id_{i}": storage.user_id,
            f"food_id_{i}": storage.food_id,
            f"quantity_{i}": storage.quantity,
            f"added_at_{i}": datetime.now(timezone.utc)
        }.items()
    }

    await session.execute(query, params)
    await session.commit()

# 冷蔵庫に食材を一件追加
async def add_storage(session: AsyncSession, user_id: int, food_id: int, quantity: float):
    query = text(
        "INSERT INTO storages (user_id, food_id, quantity, added_at) " +
        "VALUES (:user_id, :food_id, :quantity, current_timestamp)"
    )
    await session.execute(query, {"user_id": user_id, "food_id": food_id, "quantity": quantity})
    await session.commit()

# user_idから冷蔵庫のすべての食材を取得（同じ食材も分けて表示）（foodとjoin）
async def get_storage(session: AsyncSession, user_id: int) -> list[StorageWithFoodInfo]:
    query = text(
        "SELECT " + 
        "storages.id AS storage_id, " +
        "foods.id AS food_id, foods.name, foods.unit, " +
        "storages.quantity, storages.added_at " +
        "FROM storages " +
        "LEFT JOIN foods ON storages.food_id = foods.id " +
        "WHERE storages.user_id = :user_id " +
        "ORDER BY storages.added_at"
    )
    result = await session.execute(query, {"user_id": user_id})
    storage_results = result.fetchall()

    storage = [
        StorageWithFoodInfo(
            storage_id=row[0],
            food_id=row[1],
            name=row[2],
            unit=row[3],
            quantity=row[4],
            added_at=row[5]
        )
        for row in storage_results
    ]
    print("storage:", storage) #
    return storage


# user_idから冷蔵庫のすべての食材を取得 (同じ食材はまとめる)（foodとjoin）
async def get_storage_summary(session: AsyncSession, user_id: int) -> list[StorageSummaryWithFoodInfo]:
    query = text(
        "SELECT " + 
        "foods.id AS food_id, foods.name, foods.unit, " +
        "SUM(storages.quantity) AS total_quantity, " + 
        "MIN(storages.added_at) AS earliest_added_at " +
        "FROM storages " +
        "LEFT JOIN foods ON storages.food_id = foods.id " +
        "WHERE storages.user_id = :user_id " +
        "GROUP BY foods.id, foods.name, foods.unit " +
        "ORDER BY earliest_added_at"
    )
    result = await session.execute(query, {"user_id": user_id})
    storage_results = result.fetchall()

    storage = [
        StorageSummaryWithFoodInfo(
            food_id=row[0],
            name=row[1],
            unit=row[2],
            total_quantity=row[3],
            earliest_added_at=row[4]
        )
        for row in storage_results
    ]
    return storage

# 冷蔵庫の食材の詳細（それぞれの買った日、残っている量）を取得
async def get_storage_by_food(session: AsyncSession, user_id: int, food_id: int) -> list[FoodInStorage]:
    query = text(
        "SELECT " +
        "storages.id AS storage_id, " +
        "foods.id AS food_id, " + 
        "foods.name, foods.unit, storages.added_at, storages.quantity " +
        "FROM storages " +
        "LEFT JOIN foods ON storages.food_id = foods.id " +
        "WHERE storages.user_id = :user_id " +
        "AND storages.food_id = :food_id " +
        "ORDER BY storages.added_at"
    )
    result = await session.execute(query, {"user_id": user_id, "food_id": food_id})
    storage_foods_results = result.fetchall()

    storage_foods = [
        FoodInStorage(
            id=row[0],
            food_id=row[1],
            name=row[2],
            unit=row[3],
            added_at=row[4],
            quantity=row[5]
        )
        for row in storage_foods_results
    ]
    return storage_foods

# 冷蔵庫の食材の詳細（それぞれの買った日、残っている量）を取得（名前、単位はなし）
async def get_storage_food(session: AsyncSession, user_id: int, food_id: int) -> list[StorageFood]:
    query = text(
        "SELECT " +
        "id, food_id, " + 
        "added_at, quantity " +
        "FROM storages " +
        "WHERE user_id = :user_id " +
        "AND food_id = :food_id " +
        "ORDER BY added_at"
    )
    result = await session.execute(query, {"user_id": user_id, "food_id": food_id})
    storage_foods_results = result.fetchall()

    storage_foods = [
        StorageFood(
            id=row[0],
            food_id=row[1],
            added_at=row[4],
            quantity=row[5]
        )
        for row in storage_foods_results
    ]
    return storage_foods

# 冷蔵庫の特定の食材を削除
async def delete_storage(session: AsyncSession, storage_id: int):
    query = text(
        "DELETE FROM storages " +
        "WHERE id = :storage_id"
    )
    await session.execute(query, {"storage_id": storage_id})
    await session.commit()

# 冷蔵庫の食材の量を更新（減らす）
async def update_storage(session: AsyncSession, storage_id: int, quantity: float):
    query = text(
        "UPDATE storages " +
        "SET quantity = :quantity " +
        "WHERE id = :storage_id"
    )
    await session.execute(query, {"storage_id": storage_id, "quantity": quantity})
    await session.commit()


