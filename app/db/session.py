from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

# Cambiar a PostgreSQL u otro si es necesario
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with SessionLocal() as session:
        yield session
