import openai
import os
import aiohttp
import asyncio
import json
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from crud.foods import get_foods
from database import get_session, Engine
from schemas import StorageWithFoodInfo, RecipeSuggestion

openai.api_key = os.getenv('OPENAI_API_KEY')

async def load_food_data(session: AsyncSession):
    foods = await get_foods(session)
    return {food.name: {"id": food.id, "unit": food.unit} for food in foods}

async def generate_recipe(ingredients: list[StorageWithFoodInfo], num_servings: int, uses_storages_only: str, comment: str, session: AsyncSession) -> RecipeSuggestion:
    
    print("OPENAI_API_KEY", os.getenv('OPENAI_API_KEY'))
    food_data = await load_food_data(session)

    ingredient_list = "\n".join([
        f"{{\"food_id\": {food_data[item.name]['id']}, \"name\": \"{item.name}\", \"quantity\": {item.quantity}, \"unit\": \"{item.unit}\", \"added_at\": \"{item.added_at}\"}}"
        for item in ingredients
    ])
    
    prompt_message = f"""
    これらの食材を使用して作れるレシピを教えてください。以下は食材のリストです：
    {ingredient_list}

    このレシピは {num_servings} 人前です。
    冷蔵庫の中身だけを使うかどうか: {uses_storages_only}
    コメント: {comment}

    食材のadded_atが昔の物をできるだけ使ってください。
    食材の選択肢はfoodsテーブルにあるもののみから選んでください。

    レシピの手順をJSONフォーマットで出力してください。
    答えだけを出力してください。
    食材の名前は日本語にしてください。
    JSONのvalueは数値のみで、単位は別のKEYのValueとして持つようにしてください。
    例: 
    {{
        "title": "野菜たっぷりの煮込み料理",
        "foods": [
            {{
                "food_id": 1,
                "name": "ピーマン",
                "quantity": 2,
                "unit": "個"
            }},
            {{
                "food_id": 2,
                "name": "にんじん",
                "quantity": 3,
                "unit": "本"
            }},
            {{
                "food_id": 3,
                "name": "トマト",
                "quantity": 7,
                "unit": "個"
            }},
            {{
                "food_id": 4,
                "name": "ブロッコリー",
                "quantity": 1,
                "unit": "個"
            }},
            {{
                "food_id": 5,
                "name": "かぼちゃ",
                "quantity": 1,
                "unit": "個"
            }},
            {{
                "food_id": 6,
                "name": "ほうれん草",
                "quantity": 1,
                "unit": "束"
            }},
            {{
                "food_id": 7,
                "name": "薄力小麦粉",
                "quantity": 750,
                "unit": "g"
            }}
        ],
        "content": "1. ピーマン、にんじん、トマト、ブロッコリー、かぼちゃ、ほうれん草を食べやすい大きさに切ります。 2. 鍋に少量の油を熱し、にんじんとピーマンを加えて炒めます。 3. 野菜がしんなりしたら、トマトを加えてさらに炒めます。 4. かぼちゃとブロッコリーを加え、水を足して煮込みます。 5. ほうれん草を最後に加え、しんなりするまで煮ます。 6. 薄力小麦粉を水で溶いて、煮込み料理に加え、トロミが出るまで混ぜます。"
    }}
    """

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt_message
            }
        ],
        "max_tokens": 500
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload) as response:
            response_json = await response.json()
    print('response_json:', response_json)
    content = response_json["choices"][0]["message"]["content"]
    content = content.strip("```json\n").strip("\n```")
    recipe_dict = json.loads(content)

    return recipe_dict

#if __name__ == "__main__":
    mock_data = [
        {
            "storage_id": 1,
            "food_id": 3,
            "name": "ピーマン",
            "quantity": 2,
            "unit": "個",
            "added_at": "2024-07-20"
        },
        {
            "storage_id": 2,
            "food_id": 5,
            "name": "にんじん",
            "quantity": 3,
            "unit": "本",
            "added_at": "2024-07-18"
        },
        {
            "storage_id": 3,
            "food_id": 7,
            "name": "トマト",
            "quantity": 7,
            "unit": "個",
            "added_at": "2024-07-15"
        }
    ]

    ingredients = [StorageWithFoodInfo(storage_id=item["storage_id"], food_id=item["food_id"], name=item["name"], quantity=item["quantity"], unit=item["unit"], added_at=datetime.strptime(item["added_at"], "%Y-%m-%d")) for item in mock_data]
    num_servings = 4
    uses_storages_only = "true"
    comment = "ヘルシーな料理を作りたい"

    session = AsyncSession(bind=engine)

    recipe_dict = asyncio.run(generate_recipe(ingredients, num_servings, uses_storages_only, comment, session))
    print(json.dumps(recipe_dict, indent=4, ensure_ascii=False))

    async def main():
        async with AsyncSession(engine) as session:
            # データベースから食材データを取得
            food_data = await load_food_data(session)
            # 必要な処理や関数の呼び出し
            num_servings = 4
            uses_storages_only = "true"
            comment = "ヘルシーな料理を作りたい"

            # ここで ingredients を取得するロジックを追加
            ingredients = [StorageWithFoodInfo(storage_id=1, food_id=food_data["ピーマン"]["id"], name="ピーマン", quantity=2, unit="個", added_at=datetime.now())]
            
            recipe_dict = await generate_recipe(ingredients, num_servings, uses_storages_only, comment, session)
            print(json.dumps(recipe_dict, indent=4, ensure_ascii=False))

    asyncio.run(main())








