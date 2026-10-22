# 유저 정보에는 username, email, password가 포함된다. UserCreate 모델을 작성하시오
# username은 최소 3자 이상이어야 하며, 공백이 포함되면 안 된다.
# if username = " "
# email은 이메일 형식이어야 한다.
# password는 최소 8자 이상이며, 숫자와 영문자가 1개 이상 포함되어야 한다. (pattern='^[a-zA-Z0-9_]+$')
# 위 조건을 만족하지 않으면 적절한 에러 메시지를 반환해야 한다.
# 유효성 검사를 구현하고, FastAPI 경로(/register)를 통해 해당 모델을 사용하는 API를 완성하시오.

from fastapi import FastAPI, HTTPException, Path, Query, Form
from pydantic import BaseModel, EmailStr, Field, model_validator, ValidationError
from typing import Annotated

app = FastAPI()

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8, pattern='^[a-zA-Z0-9_]+$')

    # 1. 들여쓰기를 클래스 내부(4칸)로 맞춰야 합니다.
    @model_validator(mode='before')
    @classmethod
    def check(cls, value):
        username = value.get('username')
        # username이 제공되지 않았거나 공백이 포함된 경우 예외 처리
        if username and " " in username:
            raise ValueError('이름은 공백이 포함되면 안된다')
        return value

# 2. 회원가입(Form 데이터 전송)은 @app.get 대신 @app.post를 사용해야 합니다.
@app.post("/register")
def register(
    username: str = Form(..., min_length=3), 
    email: EmailStr = Form(...), # 형식을 EmailStr로 맞춰주는 것이 좋습니다.
    password: str = Form(..., min_length=8)
):
    try:
        user = UserCreate(username=username, email=email, password=password)
        return user
    except ValidationError as e:
        # FastAPI가 ValidationError를 자동으로 422 Unprocessable Entity로 변환하지만,
        # 명시적으로 HTTP 400 에러를 던지려면 아래와 같이 처리할 수 있습니다.
        raise HTTPException(status_code=400, detail=e.errors())

