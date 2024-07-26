from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import RecipeGetOut, RecipePostOut, RecipePostIn
#from ..crud import 

router = APIRouter(
    prefix="/recipe"
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


#過去にChatGPTに提案してもらったレシピを表示
@router.get("/", response_model=RecipeGetOut)
async def create_recipe(user_id: int, num_recipe: int = 10):
    #処理
    return 

#ChatGPTにレシピの提案をしてもらう
@router.post("/", response_model=RecipePostOut)
async def update_recipe(recipe: RecipePostIn):
    #処理
    return 

#いらないレシピを削除
@router.delete("/")
async def update_recipe(recipe_id: int):
    #処理
    return 