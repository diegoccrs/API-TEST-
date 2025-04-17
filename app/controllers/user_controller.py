from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserRead
from sqlalchemy.future import select

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserRead], status_code=status.HTTP_200_OK)
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users
