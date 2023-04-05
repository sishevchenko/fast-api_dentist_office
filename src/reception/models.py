from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseMeta
from src.models import BaseModel

from src.auth.models import User
from src.service.models import Service


class Reception(BaseModel, BaseMeta):
    __tablename__ = "reception"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey(Service.id, ondelete="CASCADE"), nullable=False)
    date: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    start_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    end_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

# reception = Table(
#     "reception",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("user", ForeignKey("User.id")),
#     Column("service", ForeignKey("service.id")),
#     Column("date", TIMESTAMP, default=datetime.utcnow),
#     Column("start_time", TIMESTAMP),
#     Column("end_time", TIMESTAMP),
# )
