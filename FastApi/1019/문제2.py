from fastapi import FastAPI
from typing import Optional
app=FastAPI()

# 1) localhost:8081/search?keyword=날씨​

# 2) localhost:8081/users?page=1&size=10 이렇게 구현 (page, size 값이 없어도 돌아감) 
# localhost:8081/users?page=1&aa=3&&bb=3 넣어도 에러안남​

# 3) http://localhost:8081/calc?x=3&y=5 돌리면 8나옴

@app.get("/search")
def read1(keyword:str):
    return {"keyword":keyword}

@app.get("/users")
def read2(page:int=1, size:int=10):
    return {"page":page, "size":size}

@app.get("/calc")
def read2(x:int=3, y:int=5):
    return {x+y}