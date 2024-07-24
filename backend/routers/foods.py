from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import *
from crud import *

router = APIRouter(
    prefix="food",
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


#撮った写真から食べ物を検知し、結果を取得する
@router.get("/")
async def read_fridge(img_path: str):
    #処理
    return