from sqlalchemy.orm import Mapped, mapped_column


class BaseModel:
    id: Mapped[int] = mapped_column(primary_key=True)
