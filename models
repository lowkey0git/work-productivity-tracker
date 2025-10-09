from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from sqlalchemy import Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class WorkEntry(Base):
    __tablename__ = "work_entries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    duration_seconds = Column(Float, nullable=False)  # duration stored as seconds
    amount_of_work = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    ml_prediction = Column(String, nullable=True)  # e.g., "high_diligence" or JSON

class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    reset_token = Column(String, nullable=True)  # short-lived token for password reset
    is_active = Column(Boolean, default=True)
