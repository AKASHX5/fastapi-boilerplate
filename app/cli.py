# cli.py
import typer
import asyncio
from passlib.hash import bcrypt
from sqlalchemy import select

from app.db.database import AsyncSessionLocal
from app.models.user import User
from app.core.security import hash_password

cli = typer.Typer()


@cli.command()
def create_admin(
    email: str,
    password: str,
):
    async def run():
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(User).where(User.email == email)
            )
            existing = result.scalar_one_or_none()

            if existing:
                print("User already exists")
                return
            print("EMAIL:", email)
            print("PASSWORD RAW:", password)
            print("PASSWORD LEN:", len(password))
            print("PASSWORD BYTES LEN:", len(password.encode()))

            user = User(
                email=email,
                hashed_password=hash_password(password),
                user_type="admin"
            )
            session.add(user)
            await session.commit()
            print("Admin created")

    asyncio.run(run())


if __name__ == "__main__":
    cli()
