"""
Databse initialization script.
Creates all tables defined in models.py

Usage:
    poetry run python -m app.utils.initialize_db
"""

import asyncio
import sys # Cmnd line arguments

from sqlalchemy import text # SQLAlchemy handles raw SQL strings safely

from app.database import engine, Base
from app.models import User, Conversation, Message, MoodEntry, Assessment, Resource  # noqa: F401


async def check_connection() -> bool:
    """Test database connection."""
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            print(f"✅ Database connection successful!")
            return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False


async def create_tables() -> None:
    """Create all tables from SQLAlchemy models."""
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print(f"✅ All tables created successfully!")

        # List all created tables
        async with engine.connect() as conn:
            result = await conn.execute(text(
                "SELECT tablename FROM pg_tables WHERE schemaname = 'public'"
            ))
            tables = [row[0] for row in result]
            print(f"📋 Tables: {', '.join(tables)}")
    
    except Exception as e:
        print(f"❌ Failed to create tables: {e}")
        raise


async def drop_tables() -> None:
    """Drop all tables from the database (use with caution!)."""
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        print(f"⚠️ All tables dropped successfully!")
    except Exception as e:
        print(f"❌ Failed to drop tables: {e}")
        raise


async def init_db(reset: bool = False) -> None:
    """
    Initialize database.

    Args:
        reset (bool): If True, drop all tables before creating them
    """
    print(f"🚀 Initializing database...")
    print(f"    Engine: {engine.url}")

    # Check connection first
    if not await check_connection():
        print(f"\n💡 Make sure PostgreSQL is running and .env is configured correctly.")
        sys.exit(1)

    # Optionally reset the database
    if reset:
        print(f"\n⚠️ Resetting database (dropping all tables)...")
        await drop_tables()

    # Create tables
    print("\n📦 Creating tables...")
    await create_tables()

    print("\n✨ Database initialization complete!")


def main():
    """Entry point for the script."""
    # Check for --reset flag
    reset = "--reset" in sys.argv

    if reset:
        print("🔴 WARNING: --reset flag detected. This will DELETE all data!")
        confirm = input("   Type 'yes' to confirm: ")
        if confirm.lower() != "yes":
            print(f"   Aborted.")
            sys.exit(0)
    
    asyncio.run(init_db(reset=reset))


if __name__ == "__main__":
    main()
