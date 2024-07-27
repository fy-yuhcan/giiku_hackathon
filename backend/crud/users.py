from sqlalchemy.orm import Session
from models import User

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()
