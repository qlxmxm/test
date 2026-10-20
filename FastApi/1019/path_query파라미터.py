from fastapi import FastAPI
from typing import Optional

app=FastAPI()

item_array=[
    {"name":"fast1"},
    {"name":"fast2"},
    {"name":"fast3"}
]

#query parameter
#http://localhost:8081/items?skip=0&limit=2
#값 안적으면 default값으로 들어감
@app.get("/items")
def read_item(skip:int=0, limit:int=2):
    return item_array[skip : skip+limit]

#http://127.0.0.1:8081/items?skip=0&limit=2
#default값이 없을 경우 -> 쿼리 파라미터에 인자를 줘야함
@app.get("/items_skip")
def read_item(skip:int, limit:int):
    return item_array[skip : skip+limit]

#http://127.0.0.1:8081/items?skip=0 -> limit=None
@app.get("/items_1")
def read_item1(skip:int, limit:int=None):
    if limit:
        return item_array[skip : skip+limit]
    else:
        return {"not provide"}

#이 파라미터는 선택적! 의도가 명백히 드러남 Optional
#limit이 int일 수도 있고, 안들어오면 None일수도 있다는걸 명확히 표현
@app.get("/items_2")
def read_item1(skip:int, limit:Optional[int]=None):
    if limit:
        return item_array[skip : skip+limit]
    else:
        return {"not provide"}


#http://localhost:8081/items/aa -> item_test=None
#http://localhost:8081/items/aa?item_test= -> item_test=""
@app.get("/items/{item_id}")
def read_item3(item_id:str, item_test:str | None = None):
    if item_test:
        return {"item_id":item_id , "item_test":item_test}
    return {"item_id":item_id}

