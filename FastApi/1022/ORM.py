from sqlalchemy import create_engine, text, Column, Integer, String, Boolean, DateTime
from sqlalchemy.pool import QueuePool
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from datetime import datetime

app=FastAPI()

DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw"

#DB에 접속할 준비
engine=create_engine(DATABASE_CONN, poolclass=QueuePool)


#테이블을 만들수 있게 해주는 도구
Base=declarative_base()


#Base클래스를 상속받았기 때문에 DB테이블과 연결되는 클래스가 됨
#Base를 상속받았기 때문에 DB테이블이라고 인식함
class User(Base):
    #db에 생성될 테이블 이름
    __tablename__='user'

    id=Column(Integer, primary_key=True)
    username=Column(String(50), unique=True)
    email=Column(String(100))
    is_active=Column(Boolean, default=True)
    created_at=Column(DateTime, default=datetime.utcnow)



#등록된 테이블을 DB에 만들어줘
Base.metadata.create_all(bind=engine)