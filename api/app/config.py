import os

from dotenv import load_dotenv

load_dotenv()


def postgres_dsn() -> str | None:
    url = os.getenv("DATABASE_URL")
    if url:
        return url.replace("postgresql+asyncpg://", "postgresql://", 1)
    host = os.getenv("DB_HOST")
    if not host:
        return None
    port = os.getenv("DB_PORT", "5432")
    name = os.getenv("DB_NAME", "platform")
    user = os.getenv("DB_USER", "platform")
    password = os.getenv("DB_PASS", "platform")
    return f"postgresql://{user}:{password}@{host}:{port}/{name}"
