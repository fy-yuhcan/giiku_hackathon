from pydantic import BaseModel
from datetime import date, datetime, time
from typing import List, Literal, Union, Dict

# ここで型定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも

# class Food(BaseModel):
#     food_id: List[int]
#     name: str
#     quantity: List[int]


class FridgeBase(BaseModel):
    pass

class FridgeGetOut(FridgeBase):
    id: int
    food_id: List[int]
    user_id: int
    added_at: datetime
    quantity: List[int]

class FridgePostIn(FridgeBase):
    user_id: str

class FridgePutIn(FridgeBase):
    id: str
    food_id: List[int]
    quantity: List[int]

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