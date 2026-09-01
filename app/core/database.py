import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

db_url = (settings.DATABASE_URL or "").strip()

# If running on Render cloud and DATABASE_URL points to localhost, fallback to SQLite
is_render = os.getenv("RENDER") == "true" or os.getenv("RENDER_SERVICE_ID") is not None
if is_render and ("localhost" in db_url or "127.0.0.1" in db_url or not db_url):
    print("[*] Render environment detected without remote database. Falling back to SQLite.")
    db_url = "sqlite:///./sql_app.db"

# Fix Render PostgreSQL URL (postgres:// -> postgresql://)
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

# Handle SQLite vs PostgreSQL
connect_args = {}
if db_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    db_url,
    pool_pre_ping=True,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()