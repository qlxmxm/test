from fastapi import FastAPI

#fastapi 객체 생성
app=FastAPI()

#fastapi는 경로 패턴트리 depth를 사용해 라우트를 찾는다
#items/all 과 items/{item_id} 는 같은 경로 깊이
#트리탐색할 때 먼저 쓴게 먼저 매칭 후보로 등록된다.

@app.get("/items/all")
async def read_all():
    return {"message":"all items"}

#http://localhost:8081/items/3
#path parmeter
@app.get("/items/{item_id}")
#path parameter의 타입은 int
def read_item(item_id:int):
    return {"item_id":item_id}

#fastapi는 순차적으로 매핑하기 때문에 고정값이 있을때는 반드시 먼저쓰기



