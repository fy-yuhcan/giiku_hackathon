from fastapi import UploadFile
import base64
import requests
import openai
import os
import json
from sqlalchemy.ext.asyncio import AsyncSession
from crud.foods import get_foods

openai.api_key = os.getenv('OPENAI_API_KEY')

def encode_image(file: UploadFile):
    file.file.seek(0)  # ファイルの先頭に戻る
    return base64.b64encode(file.file.read()).decode('utf-8')

async def detect_food(base64_image, session: AsyncSession):
    prompt_message = """
    これらの画像に何の食材がそれぞれ何個またはどのくらいの量写っているかJSONのリストで出力してください。
    答えだけを出力してください。
    食材の名前は日本語にしてください。
    JSONのvalueは数値のみで、単位は別のKEYのValueとして持つようにしてください。
    例：
    [
        {
            "name": "ピーマン",
            "quantity": 2,
            "unit": "個"
        },
        {
            "name": "にんじん",
            "quantity": 3,
            "unit": "本"
        },
        {
            "name": "トマト",
            "quantity": 7,
            "unit": "個"
        },
        {
            "name": "ブロッコリー",
            "quantity": 1,
            "unit": "個"
        },
        {
            "name": "かぼちゃ",
            "quantity": 1,
            "unit": "個"
        },
        {
            "name": "ほうれん草",
            "quantity": 1,
            "unit": "束"
        },
        {
            "name": "薄力小麦粉",
            "quantity": 750,
            "unit": "g"
        }
    ]
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
                "content": [
                    {
                        "type": "text",
                        "text": prompt_message
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response.raise_for_status()

    detected_foods = response.json()["choices"][0]["message"]["content"]
    detected_foods = detected_foods.strip("```json\n").strip("\n```")
    detected_foods = json.loads(detected_foods)

    # 全件取得した食品データを参照してIDを割り振る
    foods = await get_foods(session)
    food_data = {food.name: {"id": food.id, "unit": food.unit} for food in foods}

    for item in detected_foods:
        food_name = item["name"]
        if food_name in food_data:
            item["food_id"] = food_data[food_name]["id"]
            item["unit"] = food_data[food_name]["unit"]

    return detected_foods







