from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from gpt.detection import encode_image, detect_food
import os
import shutil

router = APIRouter(
    prefix="/images",
    tags=["images"]
)

@router.post("/")
async def upload_image(upload_file: UploadFile = File(...), session: AsyncSession = Depends(get_session)):
    try:
        # ローカルに画像を保存
        image_dir = "backend/images"
        os.makedirs(image_dir, exist_ok=True)
        file_path = os.path.join(image_dir, upload_file.filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        # 画像をエンコードして食材を識別
        base64_image = encode_image(upload_file)
        detected_foods = await detect_food(base64_image, session)  # detect_foodにsessionを渡す

        return {"filename": file_path, "type": upload_file.content_type, "result": detected_foods}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






