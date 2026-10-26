from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import User
from app.db.scheme.users import UserCreate, UserUpdate

#@staticmethod, @classmethod -> 인스턴스 없이 클래스에서 바로 호출
class UserCrud:
    @staticmethod
    async def get_by_id(db:AsyncSession, user_id:int) -> User | None:
        result = await db.execute(select(User).filter(User.user_id == user_id))
        return result.scalar_one_or_none() #결과가 0이면 none, 1개면 객체, 2개이상 에러


    @staticmethod
    async def create(db:AsyncSession, user:UserCreate) -> User:
        db_user=User(**user.model_dump())  #User(email=aaa@aa.com, username=hong, pasword=1234)
        db.add(db_user) #동기 (await이 없어서)
        await db.flush() #변경사항을 insert 로 db에 전송 - commit을 안해서 롤백가능함(영구반영 안함)
        return db_user

    #put, patch
    #flush() : DB에 sql 전송하는 메소드
    @staticmethod
    async def update_by_id(db:AsyncSession, user_id:int, user:UserUpdate) -> User | None:
        db_user=await db.get(User, user_id) #select *from users where user_id=(1)
        if db_user:
            update_data=user.model_dump(exclude_unset=True) #{email:"aa@aa.com", username:'bb'....}
            # db_user.username="bb"
            # db_user.email="aa@aa.com"
            #일일히 어떤필드를 수정하고 , 몇개 필드를 수정할지 미리 알수없기 때문에
            #반복문없으면 필드마다 일일이 확인해야함
            for key, value in update_data.items():
                setattr(db_user, key, value) #골라낸 필드를 자동으로 대입
            await db.flush() #수정한 내용을 DB에 전송 (update users set username='bb'...where user_id=(1))
            return db_user 
        return None


    @staticmethod
    async def delete_by_id(db:AsyncSession, user_id:int) -> User | None:
        db_user=await db.get(User, user_id)
        if db_user:
            await db.delete(db_user) #cascade때문-> 아직 로드되지 않은 자식테이블일경우 db에서 불러와야함(동기식으로 막바로 지우면안됨)
            await db.flush()  #delete from users user_id=(1)
            return db_user  #삭제된 객체반환
        return None


    @staticmethod
    async def get_by_username(db:AsyncSession, username:str) -> User | None:
        result=await db.execute(select(User).filter(User.username == username))
        return result.scalar_one_or_none()


    @staticmethod
    async def get_by_email(db:AsyncSession, email:str) -> User | None:
        result=await db.execute(select(User).filter(User.email == email))
        return result.scalar_one_or_none()



