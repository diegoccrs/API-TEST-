from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "MyFastAPIProject"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str

    # Configuración específica para entornos
    ENVIRONMENT: str = "development"  # development, production, local
    DEBUG: bool = True


# Configuración de seguridad
JWT_SECRET: str = "supersecretkey"
JWT_EXPIRE_SECONDS: int = 10000
JWT_ALGORITHM: str = "HS256"
