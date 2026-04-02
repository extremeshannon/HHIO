"""HHIO API — health and shared MalfunctionDZ PostgreSQL checks. Static site is served by nginx."""

from fastapi import FastAPI

from app.config import postgres_dsn

app = FastAPI(
    title="Here's Hopin it Opens API",
    description="Backend endpoints; public site is static HTML from the HHIO repo.",
    version="0.1.0",
)


@app.get("/health")
async def health() -> dict:
    return {"ok": True, "service": "hhio-api"}


@app.get("/health/db")
async def health_db() -> dict:
    dsn = postgres_dsn()
    if not dsn:
        return {"ok": False, "error": "No DATABASE_URL or DB_HOST configured"}

    import asyncpg

    try:
        conn = await asyncpg.connect(dsn)
        try:
            users = await conn.fetchval("SELECT count(*)::bigint FROM platform_users")
            rigs = await conn.fetchval("SELECT count(*)::bigint FROM platform_loft_rigs")
        finally:
            await conn.close()
    except Exception as e:
        return {"ok": False, "error": str(e)}

    return {
        "ok": True,
        "shared_postgres": True,
        "platform_users_count": int(users),
        "platform_loft_rigs_count": int(rigs),
    }
