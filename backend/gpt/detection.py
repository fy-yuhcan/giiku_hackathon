from fastapi import UploadFile
import base64
import requests
import openai

openai.api_key = ""

def encode_image(file: UploadFile):
  return base64.b64encode(file.file.read()).decode('utf-8')

def detect_food(base64_image):

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

  print(response.json())