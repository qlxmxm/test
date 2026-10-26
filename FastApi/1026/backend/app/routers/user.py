from fastapi import APIRouter, Depends
from app.db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import UserService
from app.db.scheme.users import UserLogin, UserRead, UserCreate
from app.core.jwt_handler import get_password_hash

router=APIRouter(prefix="/users", tags=["User"])

@router.post("/signup", response_model=UserRead)
async def sinnup(user:UserCreate, db:AsyncSession = Depends(get_db)):
    db_user=await UserService.signup(db, user)
    return db_user



@router.post("/login", response_model=UserRead)
async def login(user:UserLogin, db:AsyncSession = Depends(get_db)):
    db_user=await UserService.login(db, user)
    return db_user