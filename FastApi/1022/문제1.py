# Pydantic 모델 UserCreate를 사용
# username 길이 4~15, email 반드시 @ 포함
# age는 0 이상이어야 함
# 유효하지 않으면 에러 발생
# - post (/users) 로 요청 -> json으로 응답받기

from sqlalchemy import create_engine, text, Column, Integer, String, Boolean, DateTime
from sqlalchemy.pool import QueuePool
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, field_validator

app=FastAPI()

class UserCreate(BaseModel):
    username:str=Field(..., min_length=4, max_length=15)
    email : EmailStr
    age : int=Field(ge=0)

@app.post("/users")
def users(user:UserCreate):
    return user
