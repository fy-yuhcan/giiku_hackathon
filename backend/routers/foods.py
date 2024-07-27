from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from database import get_session
from schemas import FoodCreate, FoodModel
from crud.foods import add_food, get_foods
from gpt.detection import encode_image, detect_food

router = APIRouter(
    prefix="/food",
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


#撮った写真から食べ物を検知し、結果を取得する　（これは画像を取得するわけじゃないかも？）
# @router.get("/", response_model=FoodGetOut)
# async def read_food(image_path: str):
#     #処理
#     return 

#ユーザーが画像を投稿する
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    base64_image = encode_image(file)
    result = detect_food(base64_image)
    return {"result": result}

#食材を一つ追加
@router.post("/", response_model=FoodCreate)
async def add_food_route(name: str, unit: str, session: AsyncSession = Depends(get_session)):
    await add_food(session, name, unit)
    return {"name": name, "unit": unit}

#全ての食材を取得
@router.get("/", response_model=list[FoodModel])
async def get_foods_route(session: AsyncSession = Depends(get_session)):
    return await get_foods(session)