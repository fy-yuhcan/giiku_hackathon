from pydantic import BaseModel
from datetime import datetime
from typing import List, Literal, Union, Dict

# ここで型定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも

# class Food(BaseModel):
#     food_id: List[int]
#     name: str
#     quantity: List[int]


class FridgeBase(BaseModel):
    food_id: int
    user_id: int
    quantity: float

class FridgeCreate(FridgeBase):
    pass

class FridgeModel(FridgeBase):
    id: int
    added_at: datetime

class FridgeUpdate(BaseModel):
    quantity: float

class FridgeWithFoodInfo(BaseModel):
    food_id: int
    name: str,
    unit: str,
    total_quantity: float,
    earliest_added_at: datetime

class FoodInFridge(BaseModel):
    id: int
    food_id: int
    name: str
    unit: str
    added_at: datetime
    quantity: float

# class FridgeGetOut(FridgeBase):
#     id: int
#     food_id: List[int]
#     user_id: int
#     added_at: datetime
#     quantity: List[int]

# class FridgePostIn(FridgeBase):
#     user_id: str

# class FridgePutIn(FridgeBase):
#     id: str
#     food_id: List[int]
#     quantity: List[int]

class RecipeModel(BaseModel):
    pass

# class RecipeGetOut(RecipeModel):
#     id: int
#     foods: List[Food]

class RecipePostIn(RecipeModel):
    user_id: int
    query: str
    is_in_fridge_only: Literal["true",  "false"]

class RecipePostOut(RecipeModel):
    text: Union[str, None] = None


class FoodCreate(BaseModel):
    name: str
    unit: str

class FoodModel(FoodCreate):
    id: int

# class FoodGetOut(FoodBase):
#     foods: List[Food]