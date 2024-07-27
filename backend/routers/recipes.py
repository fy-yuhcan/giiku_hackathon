from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from schemas import RecipeGetOut, RecipePostOut, RecipePostIn
from crud.recipes import add_recipe, get_recipes, delete_recipe
from gpt.generate_recipe import generate_recipe

router = APIRouter(
    prefix="/recipe"
)

# 過去にChatGPTに提案してもらったレシピを表示
@router.get("/", response_model=RecipeGetOut)
async def get_recipes_router(user_id: int, num_recipe: int = 10, session: AsyncSession = Depends(get_session)):
    recipes = await get_recipes(session, user_id, num_recipe)
    return {"recipes": recipes}

# ChatGPTにレシピの提案をしてもらう
@router.post("/", response_model=RecipePostOut)
async def create_recipe_router(recipe: RecipePostIn, session: AsyncSession = Depends(get_session)):
    try:
        # 食材リストを作成
        ingredients = recipe.query

        # ChatGPTにレシピ提案をリクエストする
        suggestion = await generate_recipe(ingredients)

        # レシピをデータベースに保存する処理
        db_recipe = await add_recipe(session, recipe)

        # レスポンスの生成
        return RecipePostOut(id=db_recipe.id, title=db_recipe.title, foods=suggestion["foods"], content=suggestion["content"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# いらないレシピを削除
@router.delete("/{recipe_id}")
async def delete_recipe_router(recipe_id: int, session: AsyncSession = Depends(get_session)):
    success = await delete_recipe(session, recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}
