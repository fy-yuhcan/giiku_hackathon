from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from database import SessionLocal, engine
#from .api.main import router
from routers import router
from crud import *
from models import *
from schemas import *

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)