# GET /items/{item_id}
# item_id는 파라미터(Path)로 받음 (int)
# q는 쿼리 파라미터(Query)로 받음 (선택, 기본값 None)
# 응답은 { "item_id": item_id, "q": q }

# POST /login
# username과 password를 폼 데이터(Form)로 받음
# 응답은 { "username": username, "message": "로그인 성공" }​

# POST /users/
# 사용자 정보를 Request Body(JSON)로 받음
# 사용자 모델은 name(str), age(int) 필드 포함
# 응답은 입력받은 사용자 정보 그대로 반환

from fastapi import FastAPI, status, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel
from typing import Optional
import json

app=FastAPI()

@app.get("/items/{item_id}")
def items(item_id:int, q:int | None = None):
    return { "item_id": item_id, "q": q }

@app.post("/login")
def login(username:str=Form(...), password:str=Form(...)):
    return { "username": username, "message": "로그인 성공" }

class User(BaseModel):
    username:str
    age:int

@app.post("users/")
def user(user:User):
    return {user}