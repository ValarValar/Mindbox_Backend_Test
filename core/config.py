import os
from pathlib import Path

VERSION: str = "1.0.0"

# Название проекта. Используется в Swagger-документации
PROJECT_NAME: str = os.getenv("PROJECT_NAME", "mindbox_app")
# Корень проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Настройки Postgres
POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_DB: str = os.getenv("POSTGRES_DB", "mindbox_app")
POSTGRES_USER: str = os.getenv("POSTGRES_USER", "mindbox_app")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "mindbox_app")

DATABASE_URL: str = os.getenv("DATABASE_URL", f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")
