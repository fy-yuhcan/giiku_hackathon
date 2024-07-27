from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from database import get_session
from schemas import FridgeGetOut, FridgePostIn, FridgePutIn
from crud.fridges import add_fridge, get_fridge, get_fridge_by_food, remove_fridge, update_fridge

router = APIRouter(
    prefix="/fridge"
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


# user_idから冷蔵庫のすべての食材を取得
@router.get("/{user_id}", response_model=FridgeGetOut)
async def get_fridge_router(user_id: int, session: AsyncSession = Depends(get_session)):
    return await get_fridge(session, user_id)


# user_idとfood_idから冷蔵庫に一つの食材の詳細（それぞれの買った日、残っている量）を取得
@router.get("/{user_id}/{food_id}", response_model=None)    # todo: Schema定義する！
async def get_fridge_by_food_router(user_id: int, food_id: int, session: AsyncSession = Depends(get_session)):
    return await get_fridge_by_food(session, user_id, food_id)


# 冷蔵庫に食材を追加
@router.post("/", response_model=None)
async def add_fridge_router(user_id: int, food_id: int, quantity: float, session: AsyncSession = Depends(get_session)):
    await add_fridge(session, user_id, food_id, quantity)
    return {"message": "Food added to fridge"}


# 冷蔵庫の削除を更新
@router.put("/{fridge_id}", response_model=None)
async def update_fridge_router(fridge_id: int, quantity: float, session: AsyncSession = Depends(get_session)):
    # 計算して、削除と更新のDB操作をする
    return {"message": "Fridge updated"}


# 冷蔵庫の食材を削除
@router.delete("/{fridge_id}", response_model=None)
async def delete_fridge_router(fridge_id: int, session: AsyncSession = Depends(get_session)):
    await delete_fridge(session, fridge_id)
    return {"message": "Food deleted from fridge"}