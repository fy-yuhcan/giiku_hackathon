import openai
import os
import aiohttp
import asyncio
import json
from schemas import StorageWithFoodInfo, RecipeSuggestion

openai.api_key = os.getenv('OPENAI_API_KEY')

# モックデータの作成
mock_data = [
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

async def generate_recipe(ingredients: list[StorageWithFoodInfo], num_servings: int, uses_storages_only: str, comment: str) -> RecipeSuggestion:
    # uses_storages_only の処理書く
    prompt_message = f"""
    これらの食材を使用して作れるレシピを教えてください。以下は食材のリストです：

    {ingredients}

    レシピの手順をJSONフォーマットで出力してください。
    答えだけを出力してください。
    食材の名前は日本語にしてください。
    JSONのvalueは数値のみで、単位は別のKEYのValueとして持つようにしてください。
    例: 
    {{
        "title": "野菜たっぷりの煮込み料理",
        "foods": [
            {{
                "name": "ピーマン",
                "quantity": 2,
                "unit": "個"
            }},
            {{
                "name": "にんじん",
                "quantity": 3,
                "unit": "本"
            }},
            {{
                "name": "トマト",
                "quantity": 7,
                "unit": "個"
            }},
            {{
                "name": "ブロッコリー",
                "quantity": 1,
                "unit": "個"
            }},
            {{
                "name": "かぼちゃ",
                "quantity": 1,
                "unit": "個"
            }},
            {{
                "name": "ほうれん草",
                "quantity": 1,
                "unit": "束"
            }},
            {{
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
    
    content = response_json["choices"][0]["message"]["content"]
    content = content.strip("```json\n").strip("\n```")
    recipe_dict = json.loads(content)

    return recipe_dict

if __name__ == "__main__":
    ingredients = "\n".join([f"{item['name']}: {item['quantity']}{item['unit']}" for item in mock_data])
    recipe_dict = asyncio.run(generate_recipe(ingredients))
    print(json.dumps(recipe_dict, indent=4, ensure_ascii=False))









