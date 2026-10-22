from sqlalchemy import create_engine, text, Column, Integer, String, Boolean, DateTime
from sqlalchemy.pool import QueuePool
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import declarative_base, Session
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw"

#DB에 접속할 준비 -> 실제 연결이 만들어지진 않은 상태
engine=create_engine(DATABASE_CONN, poolclass=QueuePool)


#테이블을 만들수 있게 해주는 도구 - sqlalchemy에서 모델 정의할 때 상속받는 기본 클래스
Base=declarative_base()

#테이블 생성 시, sqlalchemy가 정보 사용가능  => ORM
class Student(Base):
    __tablename__='student'
    id=Column(Integer, primary_key=True, autoincrement=True)
    stu_name=Column(String(50), unique=True, nullable=False)
    email=Column(String(100), unique=True, nullable=False)



#pydantic모델링
#클라이언트가 보내는 Json 검증
class StudentCreate(BaseModel):
    stu_name:str
    email:str


#DB 세션 관리
#세션은 연결을 직접 만들고 관리하지 않는다 -> 풀에서 커넥션을 빌려와서 ORM작업을 묶어서 처리하려고 만들었다. 
#연결을 만들고 관리하는 건 엔진의 역할!!!! 

#연결관리와 작업관리 분리함
def get_con():
    db=Session(bind=engine) #db세션 생성
    try:
        yield db

    finally:
        db.close()  #커넥션(연결객체) 풀에 반납

#Base를 상속받은 모든 클래스를 테이블로 생성해라(db url 스키마에다)
Base.metadata.create_all(bind=engine)


class StudentUpdate(BaseModel):
    stu_name:Optional[str]=None
    email:Optional[str]=None


#학생 추가(C)
# /students ->Depends(get_con)인해 세션 생성 (풀에서 커넥션을 빌림) -> orm객체로 dml조작 가능 -> 응답완료 (커넥션을 풀에 반납)
#-> 다음요청이 이 커넥션을 재사용
@app.post("/students")
def create_stu(student:StudentCreate, db:Session=Depends(get_con)):

    #db에 추가
    add_stu=Student(stu_name=student.stu_name, email=student.email)
    db.add(add_stu)  #swagger ui를 이요해서 내가 넣은값을 student테이블에 삽입해줘
    db.commit()
    db.refresh(add_stu) #db에서 다시 읽어옴 (최신값 가져옴)

    return {"id":add_stu.id, "stu_name":add_stu.stu_name, "email":add_stu.email}


#학생 조회(R)
@app.get("/students/{stu_id}")
def read_stu(stu_id:int, db:Session=Depends(get_con)):
    #student테이블에서 데이터 조회
    #select * from student where id=stu_id limit 1
    db_stu=db.query(Student).filter(Student.id == stu_id).first()
    if db_stu is None:
        raise HTTPException(status_code=404, detail="Student not Found")
    return {"id":db_stu.id, "stu_name":db_stu.stu_name, "email":db_stu.email}


#학생 수정(U)
@app.put("/studensts/{stu_id}")
def update_stu(stu_id:int, stuUpdate:StudentUpdate,  db:Session=Depends(get_con)):

    #먼저 조회를 해서 해당 객체 (id같은 학생) 가져옴 
    db_stu=db.query(Student).filter(Student.id == stu_id).first()

    #/students/1 -> stu_name:tom , email:tom@naver.com

    if db_stu is None:
        return {"error":"Student Not Found"}

    #stu_name이 있으면 수정한 stu_name을 db에 넣기
    if stuUpdate.stu_name is not None:
        db_stu.stu_name=stuUpdate.stu_name

    if stuUpdate.email is not None:
        db_stu.email=stuUpdate.email

    db.commit()  #자동으로 update실행
    db.refresh(db_stu)
    return {"id":db_stu.id, "stu_name":db_stu.stu_name, "email":db_stu.email}



#학생 삭제(D)
@app.delete("/students/{stu_id}")
def delete_stu(stu_id:int, db:Session=Depends(get_con)):

    db_stu=db.query(Student).filter(Student.id == stu_id).first()

    if db_stu is None:
        return {"error":"Student Not Found"}

    db.delete(db_stu)
    db.commit()
    return {"msg":"학생 삭제됨"}