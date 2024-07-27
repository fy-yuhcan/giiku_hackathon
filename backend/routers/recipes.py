from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import RecipeGetOut, RecipePostOut, RecipePostIn
#from ..crud import 

router = APIRouter(
    prefix="/recipe"
)

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも


#過去にChatGPTに提案してもらったレシピを表示
@router.get("/", response_model=RecipeGetOut)
async def create_recipe(user_id: int, num_recipe: int = 10):
    recipes = await get_recipes(session,user_id,num_recipe)
    return 

#ChatGPTにレシピの提案をしてもらう
@router.post("/", response_model=RecipePostOut)
async def create_recipe(recipe: RecipePostIn, session: AsyncSession = Depends(get_session)):
    try:
        # 食材リストを作成
        ingredients = recipe.query

        # ChatGPTにレシピ提案をリクエストする
        suggestion = await generate_recipe(ingredients)

        # レシピをデータベースに保存する処理
        db_recipe = await add_recipe(session, recipe)

        # レスポンスの生成
        return RecipePostOut(id=db_recipe.id, title=db_recipe.title, foods=db_recipe.foods, content=suggestion["content"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#いらないレシピを削除
@router.delete("/")
async def remove_recipe(recipe_id: int, session: AsyncSession = Depends(get_session)):
    success = await delete_recipe(session, recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}