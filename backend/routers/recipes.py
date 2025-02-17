from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from schemas import RecipeGetOut, RecipePostOut, RecipeRequest, RecipeModel, RecipeSuggestion, StorageWithFoodInfo, RecipeCreate, RecipePutIn, FoodInRecipe, RecipeFoodBase, FoodInStorage, StorageFood
from crud.recipes import add_recipe, get_recipes, delete_recipe
from crud.storages import get_storage, get_storage_by_food, get_storage_food, delete_storage, update_storage
from crud.recipefood import add_recipe_food, get_recipe_foods_info, get_recipe_foods
from gpt.generate_recipe import generate_recipe

router = APIRouter(
    prefix="/recipe"
)

# 過去にChatGPTに提案してもらったレシピを表示
@router.get("/{user_id}", response_model=list[RecipeModel])
async def get_recipes_router(user_id: int, session: AsyncSession = Depends(get_session)):
    try:
        return await get_recipes(session, user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ChatGPTにレシピの提案をしてもらう
@router.post("/", response_model=RecipePostOut)
async def create_recipe_router(recipe_request: RecipeRequest, session: AsyncSession = Depends(get_session)):
    try:
        user_id = recipe_request.user_id
        num_servings = recipe_request.num_servings
        uses_storages_only = recipe_request.uses_storages_only
        comment = recipe_request.comment

        # 食材リストを作成
        ingredients: list[StorageWithFoodInfo] = await get_storage(session, user_id)

        # ChatGPTにレシピ提案をリクエストする
        suggestion: RecipeSuggestion = await generate_recipe(ingredients, num_servings, uses_storages_only, comment, session)

        # レシピをデータベースに保存する処理
        db_recipe: RecipeModel = await add_recipe(session, 
                                                  RecipeCreate(
                                                      title=suggestion.title,
                                                      content=suggestion.content,
                                                      user_id=user_id
                                                  ))
        
        # RecipeFoodsテーブルに追加する処理
        foods: list[FoodInRecipe] = suggestion.foods
        for food in foods:
            await add_recipe_food(session, food.food_id, db_recipe.id, food.quantity)

        # レスポンスの生成
        return RecipePostOut(
            id=db_recipe.id, 
            title=db_recipe.title, 
            foods=suggestion.foods, 
            content=suggestion.content
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# レシピ　作ったボタンの処理
@router.put("/")
async def use_recipe(recipe: RecipePutIn, session: AsyncSession = Depends(get_session)):
    try:
        # recipe_idからrecipe_foodsを取得
        recipe_foods: list[RecipeFoodBase] = await get_recipe_foods(session, recipe.recipe_id)
        # storageの対応するfoodを取得
        for recipe_food in recipe_foods:
            recipe_quantity = recipe_food.quantity
            storage_foods: list[StorageFood] = await get_storage_food(session, recipe.user_id, recipe_food.food_id)

            for storage_food in storage_foods:
                storage_quantity = storage_food.quantity

                if recipe_quantity == 0:
                    break
                elif storage_quantity <= recipe_quantity:
                    # delete
                    await delete_storage(session, storage_food.id)
                    recipe_quantity -= storage_quantity
                else:   # recipe_quantity < storage_quantity
                    # subtract
                    updated_quantity = storage_quantity - recipe_quantity
                    # update
                    await update_storage(session, storage_food.id, updated_quantity)
                    break
                    

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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


