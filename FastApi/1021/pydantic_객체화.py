from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

app=FastAPI()

#BaseModel 상속-> 데이터 자동으로 검증하는 클래스가 된다.
class User(BaseModel):
    id:int
    name:str
    email:str
    age:Optional[int]=None


#pydantic model 객체화
#반드시 키값을 넣는다
user=User(id=3, name="tt", email="ww@rr.com", age=3)
print(user.name)


#api(application programming interface)
# **언패킹 
# **dict -> 딕셔너리를 키워드 인자로 풀어서 넘긴다

#dict args/ json구조로 pydantic model객체화
user1=User(**{"id":3, "name":"tt", "email":"43@aa.com", "age":3})
#풀어서 넘기면 구조가
#user1=User(id=3, name="tt", email="ww@rr.com", age=3)
print(user1.name)


#일반 json문자열 -> python dict
#JSON은 그냥 글자라서, json.loads()로 먼저 dict로 바꾼 뒤 객체로 만든다.
json1='{"id":3, "name":"tt", "email":"43@aa.com", "age":3}'
json_dict=json.loads(json1) #문자열을 -> dict
print(type(json_dict))  #<class 'dict'> 

#dict args로 pydatic model 객체화
py1=User(**json_dict)
#py1=User(id=3, name="tt", email="ww@rr.com", age=3)
print(py1.id)


#언패킹(**연산자)
def func(a,b,c):
    return a+b+c

d={"a":1,"b":3,"c":5}
print(func(**d)) # = func(a=1,b=3,c=5)