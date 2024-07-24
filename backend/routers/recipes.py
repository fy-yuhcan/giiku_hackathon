from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import *
from crud import *

router = APIRouter(
    prefix="recipe"
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


#過去にChatGPTに提案してもらったレシピを表示
@router.get("/")
async def create_fridge(user_id: int, num_recipe: int = 10):
    #処理
    return 

#ChatGPTにレシピの提案をしてもらう
@router.post("/")
async def update_fridge():
    #処理
    return 

#いらないレシピを削除
@router.delete("/")
async def update_fridge(recipe_id: int):
    #処理
    return 