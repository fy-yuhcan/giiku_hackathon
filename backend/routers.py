from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud

router = APIRouter()

# ここでルーター定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも