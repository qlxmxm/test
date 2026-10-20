# fastapi : 외부 라이브러리(설치한 패키지)
# fastapi 패키지 안에서 FastAPI라는 클래스만 가져오겠다.
from fastapi import FastAPI

# FastAPI instance 생성
# 이 객체가 웹 애플리케이션 전체를 대표함
# app는 이제 웹 서버 역할을 할 수 있는 실제 객체가 됨
app = FastAPI()

# /경로에 get요청이 들어오면, root함수 실행해!
@app.get("/")  # operation
async def root():
    return {"message": "Hello World"}  
# fastapi는 자동으로 dict -> json 변환해준다.



