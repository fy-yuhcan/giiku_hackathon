from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_session
from models import User
from pydantic import BaseModel
from passlib.context import CryptContext

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# パスワードのハッシュ化に使用するコンテキスト
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthDetails(BaseModel):
    username: str
    password: str

# ユーザーをデータベースから取得する関数
async def get_user(session: AsyncSession, username: str):
    result = await session.execute(select(User).where(User.name == username))
    user = result.scalar_one_or_none()
    return user

# パスワードの検証
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/token")
async def login_for_access_token(auth_details: AuthDetails, session: AsyncSession = Depends(get_session)):
    user = await get_user(session, auth_details.username)
    if user is None or not verify_password(auth_details.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="ユーザー名またはパスワードが違います",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"user_id": user.id}
