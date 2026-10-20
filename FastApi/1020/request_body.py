from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

#Pydantic: 데이터 검사, 알맞은 타입으로 바꿔주는 파이썬 라이브러리
#BaseModel: Pydantic에서 제공하는 데이터 검증용 클래스
#fastapi에서 json요청 body를 구조화된 데이터로 받고싶을 때, BaseModel상속이 필수

app=FastAPI()

#BaseModel 상속 => 데이터 검증(타입검사), 직렬화 가능 사용가능
class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float]=None

#함수 인자로 pydantic 모델(item)이 들어오면 json형태의 request body처리
#BaseModel을 상속한 Item임 -> Request Body로 받겠구나 라고 예측
@app.post("/items")
def create_item(item:Item):
    print(item)
    return item

#json -> dict -> json
#json => item객체 -> dict로 변환 -> 서버에 전송하고 서버는 dict를 -> json으로 바꿔서 응답해줌
@app.post("/items_test")
def item_test(item:Item):   #1. 클라이언트에서 json구조로 넘김 -> 2. fastapi가 자동으로 Item로 파싱
    item_dict=item.model_dump() #3. item객체를 dict로 변환
    if item.tax is not None:
        price1=item.price+item.tax
        item_dict.update({"price1":price1})

    return  item_dict # doct를 변환하면 fastapi가 자동으로 json으로 변환해서 응답해줌


