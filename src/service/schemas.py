from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class ServiceReed(BaseModel):
    name: str
    description: str
    date: datetime = datetime.utcnow()
    price: Decimal
    available: bool
    user_id: int


class ServiceCreate(BaseModel):
    name: str
    description: str
    date: datetime = datetime.utcnow()
    price: Decimal
    available: bool
    user_id: int


class ServiceUpdate(BaseModel):
    name: Optional[str]
    description:Optional [str]
    date: Optional[datetime] = datetime.utcnow()
    price: Optional[Decimal]
    available: Optional[bool]
    user_id: Optional[int]
