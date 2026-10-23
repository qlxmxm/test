from fastapi import FastAPI, HTTPException, Depends, status, Query, Path, Form
import jwt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import datetime
from datetime import timedelta
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import declarative_base, Session, Mapped, mapped_column, relationship
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import create_engine, text, Column, Integer, String, ForeignKey

app=FastAPI()

#DB설정
DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw1"
engine=create_engine(DATABASE_CONN, poolclass=QueuePool)
Base=declarative_base()

#ORM모델
class User(Base):
    __tablename__='user'
    #id:Mapped[int]=mapped_column(primary_key=True)
    id=Column(Integer, primary_key=True)
    username=Column(String(40), unique=True, nullable=False)
    password=Column(String(100), nullable=False)
    email=Column(String(100), unique=True, nullable=False)


class Book(Base):
    __tablename__='book'
    id=Column(Integer, primary_key=True)
    title=Column(String(40), nullable=False)
    author=Column(String(40), nullable=False)
    page=Column(Integer, nullable=False)

Base.metadata.create_all(bind=engine)


#pydantic모델
class UserCreate(BaseModel):
    username:str=Field(..., min_length=2, max_length=20)
    password:str=Field(..., min_length=4)
    email:EmailStr

class BookCreate(BaseModel):
    title:str=Field(..., min_length=2, max_length=40)
    author:str=Field(..., min_length=2, max_length=40)
    page:int=Field(..., ge=1, le=10000)

#jwt설정
SECRET_KEY="secret_key"
ALGO="HS256"
EXPIRE_MIN=30

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

#jwt함수들(토큰생성/검증)
#JWT토큰 생성
#sub:subject: 토큰의 주인
#data={"sub":"jack", "exp":"만료시간"}
def create_jwt(username:str, expire:int=EXPIRE_MIN):
    exp=datetime.datetime.utcnow() + datetime.timedelta(minutes=expire)
    payload={"sub":username, "exp":exp}
    return jwt.encode(payload, SECRET_KEY, ALGO)


#JWT토큰 검증
def verify_token(token:str):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGO]) # data={"sub":"jack", "exp":"만료시간"}
        username:str=payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="유효하지않은토큰")
        return username

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="토큰 만료됨")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰")


#회원가입
#이미 있는 사용자인지 아닌지
@app.post("/users")
async def create_user(user:UserCreate):
    with Session(engine) as db:
        if db.query(User).filter(User.username == user.username).first():
            raise HTTPException(status_code=400, detail="이미 존재하는 사용자")
        #pydantic클래스에서 쓴 값을(swagger에 넣을 값) 테이블 속성에다 저장
        new_user=User(username=user.username, password=user.password, email=user.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"id":new_user.id , "username":new_user.username}


#사용자 검색(이름/Query파라미터)
#a로 검색하면 a들어간 사용자 다 조회하려고
#/users/search?username=필수입력
@app.get("/users/search")
async def search_user(username:str=Query(...)):
    with Session(engine) as db:
        users=db.query(User).filter(User.username.contains(username)).all()
        return [{"id":i.id, "username":i.username, "email":i.email} for i in users]


@app.get("/users/{user_id}")
async def get_user(user_id:int=Path(..., ge=1)):
    with Session(engine) as db:
        user=db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="id가 일치하는 사용자 없음")
        return {"id":user.id , "username":user.username, "email":user.email}

    
#책 추가
@app.post("/books")
async def create_book(book:BookCreate):
    with Session(engine) as db:
        #Book(title="파이썬", author="홍길동", page=300})
        #model_dump() : book객체를 딕셔너리로 변환
        #**model_dump() : 딕셔너리를 키=값 
        new_book=Book(**book.model_dump())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return {"id":new_book.id , "title":new_book.title}


#JWT토큰발급
@app.post("/token")
async def login_access(username:str=Form(...), password:str=Form(...)):
    with Session(engine) as db:
        user=db.query(User).filter(User.username == username).first()
        if not user or user.password!=password:
            raise HTTPException(status_code=401, detail="아이디 또는 비밀번호에서 오류남")
        #토큰생성
        token=create_jwt(username)
        return {"access_token":token, "token_type":"bearer"}


#JWT토큰이 검증된 사람들만 책을 조회할 수 있다
@app.get("/security/book/{book_id}")
async def security_book(book_id:int, token:str=Depends(oauth2_scheme)):
    username=verify_token(token) #검증확인됨

    with Session(engine) as db:
        book=db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail="책 없음")
        return{
            "book_id":book.id,
            "title":book.title,
            "username":username
        }

