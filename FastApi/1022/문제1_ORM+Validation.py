from sqlalchemy import create_engine, text, Column, Integer, String, Boolean, DateTime
from sqlalchemy.pool import QueuePool
from fastapi import FastAPI, Depends, HTTPException, Query, Path
from sqlalchemy.orm import declarative_base, Session
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

app=FastAPI()

DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw1"

#DB에 접속할 준비 -> 실제 연결이 만들어지진 않은 상태
engine=create_engine(DATABASE_CONN, poolclass=QueuePool)


#테이블을 만들수 있게 해주는 도구 - sqlalchemy에서 모델 정의할 때 상속받는 기본 클래스
Base=declarative_base()

class Items(Base):
    __tablename__='items'

    id=Column(Integer, primary_key=True)
    name=Column(String(50), nullable=False)
    print=Column(float(), nullable=False)
    quantity=Column(Integer, nullable=False)

class ItemCreate(BaseModel):
    name: str = Field(
        ..., 
        min_length=3, 
        max_length=50, 
        pattern=r'^[a-zA-Z0-9]'
    )
    # 0 초과 (gt = Greater Than)
    price: float = Field(
        ..., 
        gt=0
    )
    # 1 이상 100 이하 (ge = Greater than or Equal / le = Less than or Equal)
    quantity: int = Field(
        ..., 
        ge=1, 
        le=100
    )

#db세션관리
def get_con():
    db=Session(bind=engine) #db세션 생성
    try:
        yield db

    finally:
        db.close()  #커넥션(연결객체) 풀에 반납


Base.metadata.create_all(bind=engine)

@app.post("/items")
async def create_item(item:ItemCreate, db:Session=Depends(get_con)):
    add_item=Items(name=item.name, price=item.price, quantity=item.quantity)
    db.add(add_item)
    db.commit()
    db.refresh(add_item) #생성된 정보 갱신

    return {"id": add_item, "name": add_item.name, "quantity":add_item.quantity}

# @app.get("/items")
# async def read_total(min_price:float=Query(None, ge=0),
#                      max_price:float=Query(None,ge=0), db:Session=Depends(get_con)
#                      ):
    
@app.get("/items/{item_id}")
async def read_item(item_id:int=Path(..., ge=1), db:Session=Depends(get_con)):
    db_item=db.query(Items).filter(Items.id == item_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"id":db_item.id, "name":db_item.name, "quantity":db_item.quantity}



