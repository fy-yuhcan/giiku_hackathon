from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import FridgeGetOut, FridgePostIn, FridgePutIn
#from ..crud import 

router = APIRouter(
    prefix="/fridge"
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


#冷蔵庫を取得
@router.get("/", response_model=FridgeGetOut)
async def read_fridge(user_id: int):
    #処理
    return

#冷蔵庫を作成(アカウント作成時)
@router.post("/")
async def create_fridge(fridge: FridgePostIn):
    #処理
    return 

#冷蔵庫の状態を更新
@router.put("/")
async def update_fridge(fridge: FridgePutIn):
    #処理
    return 