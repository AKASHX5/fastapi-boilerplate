from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from passlib.hash import bcrypt

from app.core.security import verify_password, create_access_token
# ... standard login logic ...
from app.db.database import AsyncSessionLocal
from sqlalchemy import select
from app.models.user import User


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form.get("username"), form.get("password")
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(User).where(User.email == email)
            )
            user = result.scalar_one_or_none()

            if not user:
                return False
            if user.user_type != "admin":
                return False
            if not verify_password(password, user.hashed_password):
                return False

            request.session.update({"admin_id": user.id})
            return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request):
        admin_id = request.session.get("admin_id")
        if not admin_id:
            return None
        return True
