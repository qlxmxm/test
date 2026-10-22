from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, model_validator

app = FastAPI()

userdata=[{"username":"juli", "email":"aa@naver.com", "age":33},
          {"username":"tom", "email":"bb@naver.com", "age":23},
          {"username":"jack", "email":"cc@naver.com", "age":32}]



#pydantic모델
class User(BaseModel):
    #최소길이 2, 최대 20
    username:str=Field(..., min_length=2, max_length=20)
    email:EmailStr
    age:int=Field(..., ge=0, le=130)


    #모델 생성 전(객체 생성 직전) 검증
    #애초에 넣지 말아야할 것들
    @model_validator(mode="before")
    @classmethod
    def check_username(cls, values):
        username=values.get('username') #새로 입력한 값
        #입력한 username과 userdata에 있는 username비교 -> 
        # userdata에서 username이 같은게 하나라도 있으면 
        if any(i['username'] == username for i in userdata):
            raise ValueError("이미 있는 이름이다")
        return values


#POST /users 사용자 등록
@app.post("/users")
def create_user(user:User):
    userdata.append(user.model_dump())
    return {"msg":"새 사용자 등록"}

#GET /users/{username} - 사용자 조회
@app.get("/users/{username}")
def get_user(username:str):
    for i in userdata:
        if i['username']==username:
            return i
    raise HTTPException(status_code=404, detail='사용자를 찾을 수 없다')