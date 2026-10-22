from fastapi import FastAPI, Form, status
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


app=FastAPI()

#객체를 만들때 자동으로 검증됨
class User(BaseModel):
    name:str=Field(...,description='username',examples='juli')
    email:str=Field(...,description='useremail',examples='juli@naver.com')
    password:str=Field(..., min_length=8, description="userpw")
    age:Optional[int]=Field(None, ge=0, le=110) #0이상 110이하
    is_bool:bool=Field(True, examples=True)


try:
    user=User(name="juli", email="aa@ff.com", password="123458", age=120)
    print(user)

except ValidationError as e:
    print(e)