from fastapi import FastAPI, APIRouter
from pydantic import BaseModel


#경로를 묶어 관리가능-> 라우터 객체 만듬
router=APIRouter(prefix="/item", tags=["item"])


class Item(BaseModel):
    name:str
    desc:str=None


#데코레이터 함수
@router.get("/{item_id}")
def read_item(item_id:int):
    return {"item_id":item_id}


@router.post("/")
def create_item(item:Item):
    return item  #받은 객체를 그대로 반환하면 fastapi가 json으로 바꿔서 응답한다
