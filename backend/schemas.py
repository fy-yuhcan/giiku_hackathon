from pydantic import BaseModel
from datetime import datetime
from typing import List, Literal, Union, Dict

# Food関連の定義
class FoodBase(BaseModel):
    name: str
    unit: str

class FoodCreate(FoodBase):
    pass

class FoodModel(FoodBase):
    id: int

class FoodGetOut(FoodBase):
    foods: List[FoodModel]

# RecipeFoods (RecipesとFoodsの中間テーブル) 関連のスキーマ

class RecipeFoodBase(BaseModel):
    food_id: int
    quantity: float

class RecipeFoodCreate(RecipeFoodBase):
    recipe_id: int

class RecipeFoodModel(RecipeFoodCreate):
    id: int

class FoodInRecipe(BaseModel):
    food_id: int
    name: str
    quantity: int
    unit: str

# Storageベースクラス
class StorageBase(BaseModel):
    food_id: int
    user_id: int
    quantity: float

class StorageCreate(StorageBase):
    pass

class FoodInStoragePost(BaseModel):
    food_id: int
    quantity: float

class StoragePost(BaseModel):
    user_id: int
    foods: list[FoodInStoragePost]

class StorageModel(StorageBase):
    id: int
    added_at: datetime

class StorageUpdate(BaseModel):
    id: int
    quantity: float

class StorageWithFoodInfo(BaseModel):
    storage_id: int
    food_id: int
    name: str
    unit: str
    quantity: float
    added_at: datetime

class StorageSummaryWithFoodInfo(BaseModel):
    food_id: int
    name: str
    unit: str
    total_quantity: float
    earliest_added_at: datetime

class FoodInStorage(BaseModel):
    id: int
    food_id: int
    name: str
    unit: str
    added_at: datetime
    quantity: float

class StorageFood(BaseModel):
    id: int
    food_id: int
    added_at: datetime
    quantity: float

class StorageGetOut(BaseModel):
    foods: List[FoodInStorage]

class StoragePostIn(BaseModel):
    food_id: int
    user_id: int
    quantity: float

class StoragePutIn(BaseModel):
    quantity: float

# Recipe関連の定義
class RecipeBase(BaseModel):
    title: str
    content: str

class RecipeCreate(RecipeBase):
    user_id: int

class RecipeModel(RecipeBase):
    id: int

class RecipeGetOut(RecipeModel):
    foods: List[FoodInStorage]

class RecipeRequest(BaseModel):
    user_id: int
    num_servings: int
    uses_storages_only: Literal["true",  "false"]
    comment: str

class RecipeSuggestion(BaseModel):
    title: str
    foods: list[FoodInRecipe]
    content: str

class RecipePostOut(RecipeSuggestion):
    id: int

class RecipePutIn(BaseModel):
    user_id: int
    recipe_id: int

# userのスキーマ(?)違ったら変更してください
class UserBase(BaseModel):
    name: str

class User(UserBase):
    id: int
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None