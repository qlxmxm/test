from fastapi import FastAPI, Form, status
from pydantic import BaseModel, field_validator, model_validator, ValidationError
from typing import Optional
from decimal import Decimal

app=FastAPI()

#pydatic 검증 
# 1. Field()  : 간단한 조건 
# 2. @field_validator : 필드 하나 검사 - 함수 -cls, value
# 3. @model_validator : 객체 전체 검사 - 함수 -self

class Profile(BaseModel):
    name:str
    password:str
    password2:str

    #검증은 객체만들어지기 전에 일어나서 아직 self가 없다
    #클래스(cls),검사할 값(value)
    #name 필드 들어올때마다 실행하는 함수
    @field_validator('name')
    @classmethod
    def name1(cls, value:str):
        if not value.strip():
            raise ValueError('값이 비어있으면 안된다')
        return value


    @field_validator('password')
    @classmethod
    def pw1(cls, value:str):
        if len(value)<5:
            raise ValueError('비번 5글자 이상어야한다.')
        return value


    @model_validator(mode='after') #객체 생성된 이후 필드 비교
    def after1(self):  #클래스 전체 상태를 보려고 인스턴스가 넘어온다
        if self.password != self.password2:
            raise ValueError('두개 비밀번호 같지 않아')
        return self


try:
    profile=Profile(name="abc", password="12345", password2="12345")
    print(profile)

except ValidationError as e:
    print(e)