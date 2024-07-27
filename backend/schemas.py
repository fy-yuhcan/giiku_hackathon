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
    quantity: float

class StorageWithFoodInfo(BaseModel):
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
class RecipeModel(BaseModel):
    pass

class RecipeGetOut(RecipeModel):
    id: int
    foods: List[FoodInStorage]

class RecipePostIn(RecipeModel):
    user_id: int
    query: str
    is_in_storage_only: Literal["true",  "false"]

class RecipePostOut(RecipeModel):
    text: Union[str, None] = None

class RecipeRequest(BaseModel):
    user_id: int
    num_servings: int
    uses_storages_only: bool
    comment: str

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