from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

#Pydantic: 데이터 검사, 알맞은 타입으로 바꿔주는 파이썬 라이브러리
#BaseModel: Pydantic에서 제공하는 데이터 검증용 클래스
#fastapi에서 json요청 body를 구조화된 데이터로 받고싶을 때, BaseModel상속이 필수

app=FastAPI()

class Item(BaseModel):
    name:str
    price:int
    desc:Optional[str]=None

class User(BaseModel):
    username:str
    age:Optional[int]=None

#path parmeter, request body parameter 처리
#라우트 정의 : PUT/item_test/123

@app.put("/item_test/{item_id}")
def update_item(item_id:int, item:Item, user:User):
    results={"item_id":item_id, "item":item, "user":user}
    return results

#json(데이터 교환포멧) dict(파이썬 자료형 - 파이썬 내부에만 존재) 차이
#클라이언트가 보낼때 json -> fastapi(python dict로 변환) -> 서버사 dict로 반환하면 클라이언트한테 자동으로 json으로 응답함




