from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, TIMESTAMP, ForeignKey

metadata = MetaData()

reception = Table(
    "reception",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user", ForeignKey("User.id")),
    Column("service", ForeignKey("service.id")),
    Column("date", TIMESTAMP, default=datetime.utcnow),
    Column("start_time", TIMESTAMP),
    Column("end_time", TIMESTAMP),
)
