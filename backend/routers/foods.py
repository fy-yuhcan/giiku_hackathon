from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from ..schemas import FoodGetIn, FoodGetOut
from ..crud import *
from ..gpt.detection import encode_image, detect_food

router = APIRouter(
    prefix="food",
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


#撮った写真から食べ物を検知し、結果を取得する　（これは画像を取得するわけじゃないかも？）
@router.get("/", response_model=FoodGetOut)
async def read_food(image_path: str):
    #処理
    return 

#ユーザーが画像を投稿する
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    base64_image = encode_image(file)
    result = detect_food(base64_image)
    return {"result": result}