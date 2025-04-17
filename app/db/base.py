from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime, func


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
