from fastapi import APIRouter, UploadFile, HTTPException
import shutil
from pathlib import Path
from gpt.detection import detect_food, encode_image

router = APIRouter(
    prefix="/images",
    tags=["images"]
)

# 画像をアップロードして保存し、detection.pyに送信する
@router.post("/")
async def upload_image(upload_file: UploadFile):
    # 保存先のディレクトリ
    save_directory = Path("backend/images")
    save_directory.mkdir(parents=True, exist_ok=True)
    
    # ファイルのパス
    file_path = save_directory / upload_file.filename
    
    # ファイルを保存
    with open(file_path, 'wb+') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    # 画像をエンコードしてdetection.pyに送信
    try:
        encoded_image = encode_image(upload_file)
        detection_result = detect_food(encoded_image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "filename": str(file_path),
        "type": upload_file.content_type,
        "detection_result": detection_result
    }
