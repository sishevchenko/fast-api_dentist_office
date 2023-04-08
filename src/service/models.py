from decimal import Decimal
from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey, Boolean, DECIMAL, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseMeta
from src.models import BaseModel

from src.auth.models import User


class Service(BaseModel, BaseMeta):
    __tablename__ = "service"

    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    price: Mapped[Decimal] = mapped_column(DECIMAL)
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"), nullable=False)

    def __str__(self):
        return f"{self.name} - {self.price} руб."
