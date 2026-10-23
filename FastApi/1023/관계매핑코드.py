from fastapi import FastAPI, HTTPException, Depends, status, Query, Path, Form
import jwt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import datetime
from datetime import timedelta
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import declarative_base, Session, Mapped, mapped_column, relationship, DeclarativeBase, sessionmaker
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import create_engine, text, Column, Integer, String, ForeignKey

app=FastAPI()

DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw"

#엔진 생성
#sqlalchemy에서 데이터베이스 연결 객체를 생성하는 함수
#poolclass=QueuePool : 매번 DB연결 안하고 미리 연결 만들어서 재사용하려고(성능 up, 속도 up)
engine=create_engine(DATABASE_CONN)

SessionLocal=sessionmaker(bind=engine)


Base=declarative_base()

class Author(Base):
    __tablename__='authors'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(50))

    #author가 쓴 Book객체들의 리스트  = relationship("연결할클래스명")
    #back_populates : Book클래스에서 반대 관계를 연결하는 필드명
    #author.books 로 책 리스트 가져올수있음
    books:Mapped[list["Book"]]=relationship("Book", back_populates="author")


class Book(Base):
    __tablename__='books'
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(50))
    author_id:Mapped[int]=mapped_column(ForeignKey("authors.id"))

    author:Mapped["Author"]=relationship("Author", back_populates="books")

#테이블 생성코드
#db의존성 코드
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()   

@app.get("/books")
def get_books(db:Session=Depends(get_db)):
    stmt=select(Book, Author).join(Author)
    result=db.execute(stmt).all()
    for i,j in result:
        print(i.title,j.name)








