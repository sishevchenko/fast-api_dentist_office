from datetime import datetime

from sqlalchemy import String, JSON, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from src.database import BaseMeta
from src.models import BaseModel


class Status(BaseModel, BaseMeta):
    __tablename__ = "status"

    name: Mapped[str] = mapped_column(String, nullable=False)
    permissions: Mapped[JSON] = mapped_column(JSON)

    def __str__(self):
        return f"{self.name}"


class User(SQLAlchemyBaseUserTable[int], BaseModel, BaseMeta):
    username: Mapped[str] = mapped_column(String(length=100), nullable=False, )
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    status_id: Mapped[int] = mapped_column(ForeignKey("status.id"))

    def __str__(self):
        return f"{self.username}"

# status = Table(
#     "status",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("permissions", JSON),
# )
#
# user = Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("email", String, nullable=False),
#     Column("username", String, nullable=False),
#     Column("hashed_password", String, nullable=False),
#     Column("registered_at", TIMESTAMP, default=datetime.utcnow),
#     Column("status_id", Integer, ForeignKey("status.id")),
#     Column("is_active", Boolean, default=True, nullable=False),
#     Column("is_superuser", Boolean, default=False, nullable=False),
#     Column("is_verified", Boolean, default=False, nullable=False),
# )
