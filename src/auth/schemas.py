from datetime import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    email: str
    username: str
    registered_at: datetime = datetime.utcnow()
    status_id: int


class UserCreate(schemas.BaseUserCreate):
    email: str
    username: str
    password: str
    registered_at: datetime = datetime.utcnow()
    status_id: int = 1


class UserUpdate(schemas.BaseUserUpdate):
    email: Optional[str]
    username: Optional[str]
    password: Optional[str]
    registered_at: Optional[datetime]
    status_id: Optional[int]
