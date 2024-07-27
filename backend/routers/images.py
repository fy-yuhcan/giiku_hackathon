from fastapi import APIRouter, UploadFile, HTTPException, Depends
import shutil
import os
from gpt.detection import encode_image, detect_food

router = APIRouter()

@router.post("/images/")
async def upload_image(upload_file: UploadFile):
    try:
        # 画像を保存するディレクトリ
        save_dir = "images"
        os.makedirs(save_dir, exist_ok=True)
        
        # ファイルパスを指定
        file_path = os.path.join(save_dir, upload_file.filename)
        
        # 画像を保存
        with open(file_path, 'wb+') as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        # 画像をbase64にエンコード
        base64_image = encode_image(upload_file)
        
        # OpenAI APIで画像を解析
        result = detect_food(base64_image)

        return {
            "filename": file_path,
            "type": upload_file.content_type,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


