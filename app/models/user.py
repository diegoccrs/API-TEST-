from sqlalchemy import Column, String
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
