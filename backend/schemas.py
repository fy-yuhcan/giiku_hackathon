from pydantic import BaseModel
from datetime import datetime
from typing import List, Literal, Union, Dict

# Storageベースクラス
class StorageBase(BaseModel):
    food_id: int
    user_id: int
    quantity: float

class StorageCreate(StorageBase):
    pass

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

class RecipeCreate(BaseModel):
    user_id: int

class RecipeModel(RecipeBase):
    id: int

class RecipeGetOut(RecipeModel):
    foods: List[FoodInStorage]

class RecipeRequest(BaseModel):
    user_id: int
    num_servings: int
    is_in_storage_only: Literal["true",  "false"]
    comment: str

class RecipeSuggestion(BaseModel):
    pass

class RecipePostOut(RecipeModel):
    text: Union[str, None] = None

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

class FoodInRecipe(FoodModel):
    quantity: int

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