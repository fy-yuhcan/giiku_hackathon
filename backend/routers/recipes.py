from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from schemas import RecipeGetOut, RecipePostOut, RecipeRequest, RecipeModel, RecipeSuggestion, StorageWithFoodInfo, RecipeCreate
from crud.recipes import add_recipe, get_recipes, delete_recipe
from crud.storages import get_storage
from gpt.generate_recipe import generate_recipe

router = APIRouter(
    prefix="/recipe"
)

# 過去にChatGPTに提案してもらったレシピを表示
@router.get("/", response_model=RecipeGetOut)
async def get_recipes_router(user_id: int, num_recipe: int = 10, session: AsyncSession = Depends(get_session)):
    try:
        recipes = await get_recipes(session, user_id, num_recipe)
        return {"recipes": recipes}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ChatGPTにレシピの提案をしてもらう
@router.post("/", response_model=None)      # あとでスキーマ定義する！
async def create_recipe_router(recipe_request: RecipeRequest, session: AsyncSession = Depends(get_session)):
    try:
        user_id = recipe_request.user_id
        num_servings = recipe_request.num_servings
        uses_storages_only = recipe_request.uses_storages_only
        comment = recipe_request.comment

        # 食材リストを作成
        ingredients: list[StorageWithFoodInfo] = await get_storage(session, user_id)

        # ChatGPTにレシピ提案をリクエストする
        suggestion: RecipeSuggestion = await generate_recipe(ingredients, num_servings, uses_storages_only, comment)

        # レシピをデータベースに保存する処理
        db_recipe: RecipeModel = await add_recipe(session, 
                                                  RecipeCreate(
                                                      title=suggestion.title,
                                                      content=suggestion.content,
                                                      user_id=user_id
                                                  ))
        
        # RecipeFoodsテーブルに追加する処理

        # レスポンスの生成
        return RecipePostOut(
            id=db_recipe.id, 
            title=db_recipe.title, 
            foods=suggestion["foods"], 
            content=suggestion["content"]
        )  # 直す！

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# レシピ　作ったボタンの処理

# いらないレシピを削除
@router.delete("/{recipe_id}")
async def delete_recipe_router(recipe_id: int, session: AsyncSession = Depends(get_session)):
    try:
        success = await delete_recipe(session, recipe_id)
        if not success:
            raise HTTPException(status_code=404, detail="Recipe not found")
        return {"message": "Recipe deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
