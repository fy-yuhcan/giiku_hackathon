from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, DateTime
from sqlalchemy.orm import relationship

from database import Base

# ここでデータベースのテーブル定義
# コード増えそうだったらディレクトリ作ってファイル分けてもいいかも