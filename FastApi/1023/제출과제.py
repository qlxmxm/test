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

#1. 데이터베이스 연결
DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw1"
engine=create_engine(DATABASE_CONN, poolclass=QueuePool)
Base=declarative_base()

#2. ORM 모델
#Student - id(primary_key,Integer) - name(String, 20자) - age(Integer)
class Student(Base):
    __tablename__='student'
    id=Column(Integer, primary_key=True)
    name=Column(String(20))
    age=Column(Integer)

#Course - id(primary_key,Integer) - title(String, 30자) - student_id(ForeignKey -> Student.id)
class Course(Base):
    __tablename__='course'
    id=Column(Integer, primary_key=True)
    title=Column(String(30))
    student_id=Column(ForeignKey("student.id"))

Base.metadata.create_all(bind=engine)


#3. pydantic모델
#StudentCreate - name:최소2자, 최대20자 - age:10~100
class StudentCreate(BaseModel):
    name:str=Field(..., min_length=2, max_length=20)
    age:int=Field(..., ge=10, le=100)
#CourseCreate - title: 최소 2자, 최대 30자 - student_id: Integer
class CourseCreate(BaseModel):
    title:str=Field(..., min_length=2, max_length=30)
    student_id:int

#4. API 엔드포인트
#a. 학생 생성 Post/students 
# - 요청:Body:StudentCreate - DB에 학생 추가 후, 생성된 학생 정보 반환
@app.post("/students")
async def create_student(student:StudentCreate):
    with Session(engine) as db:
        new_student=Student(name=student.name, age=student.age)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return {
                "id":new_student.id, 
                "studentname":new_student.name,
                "studentage":new_student.age
                }

#b. 학생 전제 조회 GET/students
# - 선택적 쿼리 파라미터:age (입력 시 해당 나이 이상 학생만 반환)
@app.get("/students")
async def search_student(age:int=Query(...)):
    with Session(engine) as db:
        students=db.query(Student).filter(Student.age >= age).all()
        return [{"id":i.id, "studentname":i.name, "studentage":i.age} for i in students]

#c. 측정 학생 조회 GET/students/{id}
# - 존재하지 않으면 404 반환
@app.get("/students/{id}")
async def get_student(id:int=Path(..., ge=1)):
    with Session(engine) as db:
        student=db.query(Student).filter(Student.id == id).first()
        if not student:
            raise HTTPException(status_code=404, detail="id가 일치하는 사용자 없음")
        return {"id":student.id , "studentname":student.name, "age":student.age}

#d. 학생 삭제 DELETE/students/{id}
# - 존재하지 않으면 404 - 삭제 성공 시 {"msg":"삭제완료"} 반환
@app.delete("/students/{id}")
async def delete_student(id:int=Path(..., ge=1)):
    with Session(engine) as db:
        student=db.query(Student).filter(Student.id == id).first()
        if not student:
            raise HTTPException(status_code=404, detail="id가 일치하는 사용자 없음")
        db.delete(student)
        db.commit()
        return {"msg":"삭제 완료"}

#e. 과목 생성 POST/courses
# - 요청 Body:CourseCreate - student_id가 존재하지 않으면 404 반환 - DB에 과목 추가 후 반환
@app.post("/courses")
async def create_course(course:CourseCreate):
    with Session(engine) as db:
        student=db.query(Student).filter(Student.id == course.student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="id가 일치하는 사용자 없음")
        new_course=Course(title=course.title, student_id=course.student_id)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return {
                "id":new_course.id, 
                "title":new_course.title,
                "student_id":new_course.student_id
                }

#f. 전제 과목 조회 GET/courses
# - 선택적 쿼리 파라미터: title(부분 일치 검색)
@app.get("/courses")
async def search_courses(coursetitle:str=Query(...)):
    with Session(engine) as db:
        courses=db.query(Course).filter(Course.title.contains(coursetitle)).all()
        return [{"id":i.id, "title":i.title, "student_id":i.student_id} for i in courses]

#g. 특정 학생의 과목 조회 GET/students/{id}/courses
# - 존재하지 않으면 404
# - 반환 예시 : { "student": "홍길동", "courses":[{"id":1, "title":"수학", "student_id":1}, ...] }
@app.get("/students/{id}/courses")
async def get_student_courses(id: int = Path(..., ge=1)):
    with Session(engine) as db:
        student = db.query(Student).filter(Student.id == id).first()
        if not student:
            raise HTTPException(status_code=404, detail="id가 일치하는 사용자 없음")

        courses = db.query(Course).filter(Course.student_id == id).all()
        course_list = [{"id": i.id, "title": i.title, "student_id": i.student_id} for i in courses]

        return {
            "student": student.name,
            "courses": course_list
        }

#h. 과목 삭제 DELETE/courses/{id}
# - 존재하지 않으면 404 - 삭제 성공 시 {"msg":"삭제완료"}
@app.delete("/courses/{id}")
async def delete_course(id:int=Path(..., ge=1)):
    with Session(engine) as db:
        course=db.query(Course).filter(Course.id == id).first()
        if not course:
            raise HTTPException(status_code=404, detail="id가 일치하는 과목이 없음")
        db.delete(course)
        db.commit()
        return {"msg":"삭제 완료"}

#i. 특정 학생 과목 개수 조회 GET/student/{id}/count
# - 반환 예시 : {"student_id":1, "course_count":3}
@app.get("/student/{id}/count")
async def get_student_course_count(id: int = Path(..., ge=1)):
    with Session(engine) as db:
        student = db.query(Student).filter(Student.id == id).first()
        if not student:
            raise HTTPException(status_code=404, detail="id가 일치하는 사용자 없음")

        # func 없이 쿼리문 끝에 .count()를 붙여서 개수를 가져옵니다.
        count = db.query(Course).filter(Course.student_id == id).count()
        
        return {"student_id": id, "course_count": count}




