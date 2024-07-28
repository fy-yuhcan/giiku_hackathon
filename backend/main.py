from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session


#from database import SessionLocal, engine
#from .crud import 
#from .models import 
#from .schemas import 
from routers import foods, storages, recipes,auth,images

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(foods.router)
app.include_router(storages.router)
app.include_router(recipes.router)
app.include_router(auth.router)
app.include_router(images.router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)