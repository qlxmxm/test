# 요청은 username, password = > Form 데이터 
# 응답은 Pydantic 모델 => LoginResponse 사용 (LoginResponse 만들기) => username, msg
# 로그인 성공 시 메시지와 username 반환
# post("/login", response_model=LoginResponse)

from fastapi import FastAPI,Form
from pydantic import BaseModel
app=FastAPI()

class LoginResponse(BaseModel):
    username : str
    msg : str

@app.post('/login',response_model=LoginResponse)
async def test2(username:str=Form(...),password:str=Form(...)):
    return LoginResponse(username=username,msg='로그인 성공')
