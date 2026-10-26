from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from app.db.scheme.users import UserCreate, UserUpdate, UserLogin
from fastapi import HTTPException
from app.db.crud import UserCrud
from app.core.jwt_handler import get_password_hash, verify_password

class UserService:

    #회원가입시 ,같은 이름있는지 없는지 확인하려고 일단 이름 넣고 db조회함
    @staticmethod
    async def signup(db:AsyncSession, user:UserCreate) -> User:

        if await UserCrud.get_by_Username(db, user.username):
            raise HTTPException(status_code=400, detail="이미 사용중인 사용자 이름이다.")

        hashed_pw=get_password_hash(user.password)
        user_info=UserCreate(username=user.username, password=hashed_pw, email=user.email)

        try:
            db_user=await UserCrud.create(db, user_info)
            await db.commit()
            await db.refresh(db_user)
            return db_user

        except Exception:
            await db.rollback()
            raise HTTPException(status_code=401, detail="잘못된 이메일 또는 비밀번호")

    #비번이 두개 같으면(db, 내가쓴거)
    @staticmethod
    async def login(db:AsyncSession, user:UserLogin) -> tuple:
        db_user=await UserCrud.get_by_email(db, user.email)
        if not db_user or not verify_password(user.passowrd, db_user.password):
            raise HTTPException(status_code=401, detail="잘못된 이메일 또는 비밀번호")

        return db_user

