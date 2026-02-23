from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api.utils import get_current_user
from app.db.database import get_db
from app.models.user import User, Profile
from app.schema.user import UserResponse, UserCreate
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token
from app.schema.user import Token
from app.services.user_service import user_service
from app.core.exceptions import UserAlreadyExistsException

router = APIRouter()


@router.post('/register', response_model=UserResponse)
async def register_user(user_input:UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await user_service.get_by_email(db, email=user_input.email)
    if existing_user:
        raise UserAlreadyExistsException()  # Clean custom exception

    # 2. Use the service to do the heavy lifting
    return await user_service.register_new_user(db,
                                                user_data=user_input.model_dump())


@router.post('/login', response_model=Token)
async def login(
        db: AsyncSession = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    print('hello login',form_data)
    query = select(User).where(User.email == form_data.username)
    result = await db.execute(query)
    user = result.scalars().first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect passowrd',
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {'access_token': access_token, 'token_type': "bearer"}


@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    # This route only runs if the user provides a valid JWT
    return current_user