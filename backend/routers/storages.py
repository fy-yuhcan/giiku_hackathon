from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from schemas import StorageWithFoodInfo, FoodInStorage, StorageCreate, StorageUpdate, StoragePost, FoodInStoragePost
from crud.storages import add_storages, add_storage, get_storage_summary, get_storage_by_food, delete_storage, update_storage

router = APIRouter(
    prefix="/storage"
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも

# user_idから冷蔵庫のすべての食材を取得
@router.get("/{user_id}", response_model=list[StorageWithFoodInfo])
async def get_storage_summary_router(user_id: int, session: AsyncSession = Depends(get_session)):
    try:
        return await get_storage_summary(session, user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# user_idとfood_idから冷蔵庫に一つの食材の詳細（それぞれの買った日、残っている量）を取得
@router.get("/{user_id}/{food_id}", response_model=list[FoodInStorage])
async def get_storage_by_food_router(user_id: int, food_id: int, session: AsyncSession = Depends(get_session)):
    try:
        return await get_storage_by_food(session, user_id, food_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 冷蔵庫に食材を追加
@router.post("/", response_model=None)
async def add_storages_router(storages: StoragePost, session: AsyncSession = Depends(get_session)):
    try:
        
        foods: list[FoodInStoragePost] = storages.foods
        # storages_create: list[StorageCreate] = []
        for food in foods:
            await add_storage(session, storages.user_id, food.food_id, food.quantity)

        # データベースに追加しやすいようにデータを成形
        # foods: list[FoodInStoragePost] = storages.foods
        # storages_create: list[StorageCreate] = []
        # for food in foods:
        #     storages_create.append({
        #         "food_id": food.food_id,
        #         "user_id": storages.user_id,
        #         "quantity": food.quantity
        #     })

        # await add_storages(session, storages_create)
        return {"message": "Food added to storage"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 冷蔵庫の食材を更新
# @router.put("/", response_model=None)
# async def update_storage_router(storage: StorageUpdate, session: AsyncSession = Depends(get_session)):
#     try:
#         await update_storage(session, storage.id, storage.quantity)
#         return {"message": "Storage updated"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# 冷蔵庫の食材を削除
@router.delete("/{storage_id}", response_model=None)
async def delete_storage_router(storage_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await delete_storage(session, storage_id)
        return {"message": "Food deleted from storage"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
