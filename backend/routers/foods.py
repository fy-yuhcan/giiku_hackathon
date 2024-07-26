from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import FoodGetOut
#from ..crud import 

router = APIRouter(
    prefix="/food",
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


#撮った写真から食べ物を検知し、結果を取得する
@router.get("/", response_model=FoodGetOut)
async def read_food(image_path: str):
    #処理
    return 