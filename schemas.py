from pydantic import BaseModel, Field, validator
from datetime import datetime, timedelta
from typing import Optional

class WorkEntryCreate(BaseModel):
    name: str = Field(..., min_length=1)
    start_time: datetime
    end_time: datetime
    amount_of_work: float = Field(..., gt=0)

    @validator("end_time")
    def end_after_start(cls, v, values):
        start = values.get("start_time")
        if start is None:
            return v
        if v <= start:
            raise ValueError("end_time must be after start_time")
        return v

class WorkEntryResponse(BaseModel):
    id: int
    name: str
    start_time: datetime
    end_time: datetime
    duration_seconds: float
    amount_of_work: float
    ml_prediction: Optional[str] = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: Optional[str] = None

class ManagerCreate(BaseModel):
    username: str
    password: str
    email: Optional[str]

class ManagerOut(BaseModel):
    id: int
    username: str
    email: Optional[str]

    class Config:
        orm_mode = True

class PasswordResetRequest(BaseModel):
    username: str

class PasswordResetConfirm(BaseModel):
    username: str
    reset_token: str
    new_password: str

