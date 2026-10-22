# 1. @app.put("/items/{item_id}" 요청함 (form데이터)
# 2. fastapi가 Path, Query, Form 규칙으로 검증
# 3. 통과하면 함수실행
# 4. 객체가 만들어지고, Field규칙 수행 + validator검증 

from fastapi import FastAPI, HTTPException, Path, Query, Form
from pydantic import BaseModel, EmailStr, Field, model_validator, ValidationError
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name:str=Field(..., min_length=3, max_length=30)
    desc:str=Field(None, max_length=500)
    price:float=Field(..., ge=0)
    tax:float|None=None

    #객체 생성 후에 tax, price값을 비교해서
    #tax값이 price보다 크면 ValueError 발생
    @model_validator(mode="after")
    def check(self):
        if self.tax > self.price:
            raise ValueError('tax가 price보다 크면 안돼')
        return self




#Path() : url경로
#Query() : 쿼리스트링
#Form() : 폼 (데이터를 입력받아서 검증)
#Field() : pydantic 모델 클래스 안 검증
 
@app.put("/items/{item_id}")
def items1(item_id:int=Path(..., gt=0), 
           q1:str=Query(...,max_length=50),
           name:str=Form(..., min_length=2, max_length=30),
           desc:Annotated[str, Form(max_length=100)]=None,
           price:float=Form(..., ge=0),
           tax:Annotated[float, Form()]=None):

    try:
        item=Item(name=name, desc=desc, price=price, tax=tax)
        return item
    except ValidationError as e:
        raise e
