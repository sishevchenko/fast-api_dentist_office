from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, TIMESTAMP, ForeignKey, Boolean, DECIMAL, String

metadata = MetaData()

service = Table(
    "service",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("user", ForeignKey("User.id")),
    Column("date", TIMESTAMP, default=datetime.utcnow),
    Column("price", DECIMAL),
    Column("available", Boolean, default=True),
)
