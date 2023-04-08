from datetime import date, time

from sqlalchemy import TIMESTAMP, ForeignKey, Date, Time
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseMeta
from src.models import BaseModel

from src.auth.models import User
from src.service.models import Service


class Reception(BaseModel, BaseMeta):
    __tablename__ = "reception"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey(Service.id, ondelete="CASCADE"), nullable=False)
    recording_date: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)
    start_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"
