from sqlalchemy.orm import Session
from . import models, schemas
from datetime import timedelta
from passlib.context import CryptContext

def create_work_entry(db: Session, entry: schemas.WorkEntryCreate, ml_prediction: str = None):
    duration = (entry.end_time - entry.start_time).total_seconds()
    db_obj = models.WorkEntry(
        name=entry.name,
        start_time=entry.start_time,
        end_time=entry.end_time,
        duration_seconds=duration,
        amount_of_work=entry.amount_of_work,
        ml_prediction=ml_prediction,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_work_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.WorkEntry).offset(skip).limit(limit).all()

def get_work_entry(db: Session, entry_id: int):
    return db.query(models.WorkEntry).filter(models.WorkEntry.id == entry_id).first()

# Manager CRUD

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_manager(db: Session, username: str, password: str, email: str = None):
    hashed = pwd_context.hash(password)
    manager = models.Manager(username=username, hashed_password=hashed, email=email)
    db.add(manager)
    db.commit()
    db.refresh(manager)
    return manager

def get_manager_by_username(db: Session, username: str):
    return db.query(models.Manager).filter(models.Manager.username == username).first()

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def set_reset_token(db: Session, manager: models.Manager, token: str):
    manager.reset_token = token
    db.add(manager)
    db.commit()
    db.refresh(manager)
    return manager

def reset_password(db: Session, username: str, new_hashed_password: str):
    m = get_manager_by_username(db, username)
    if not m:
        return None
    m.hashed_password = new_hashed_password
    m.reset_token = None
    db.add(m)
    db.commit()
    db.refresh(m)
    return m
