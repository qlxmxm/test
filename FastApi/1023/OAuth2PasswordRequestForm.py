from fastapi import FastAPI, HTTPException, Depends, status
import jwt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import datetime
from datetime import timedelta


app=FastAPI()

SECRET_KEY="secret_key"
ALGO="HS256"

#사용자가 /token에서 토큰을 발급받고, api요청 시에
#Authorization 헤더에 Bearer토큰을 넣어서 인증하는 구조를 만들겠다. -> 토큰만 꺼냄
oauth_scheme=OAuth2PasswordBearer(tokenUrl="token")

user_db={"jack":{"username":"tom", "password":"1234"}}

#JWT토큰 생성
#sub:subject: 토큰의 주인
#data={"sub":"jack", "exp":"만료시간"}
def create_jwt(data:dict, expire:timedelta=None):
    exp=datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
    data["exp"]=exp
    return jwt.encode(data, SECRET_KEY, ALGO)



#JWT토큰 검증
def verify_token(token:str):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGO]) # data={"sub":"jack", "exp":"만료시간"}
        username:str=payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="유효하지않은토큰")
        return username

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="토큰 만료됨")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰")


#username, password ->  form 입력하면
#f_data.username="tom"
#f_data.password="1234"

@app.post("/token")
def login(f_data:OAuth2PasswordRequestForm=Depends()):
    user=user_db.get(f_data.username)
    if not user or user['password']!=f_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="유효하지않은토큰")

    access_token=create_jwt(data={"sub":user['username']},
                            expire=timedelta(minutes=60))

    return {"access_token":access_token, "type":"bearer"}



# Depends(oauth_scheme) : 요청 헤더 Authorization:Bearer(토큰) 에서 토큰 문자열만 뽑아 token에 넣어줌
# 이 토큰을 verify_token() 에 넘겨 검증하고 성공하면 사용자 이름을 응답한다
@app.get("/verify")
def verify(token:str=Depends(oauth_scheme)):
    username=verify_token(token)
    return {"msg":"valid token", "username":username}