from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    pass  # Si hubiera campos para crear un usuario, van aquí


class UserRead(BaseModel):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True  # Para compatibilidad con SQLAlchemy
