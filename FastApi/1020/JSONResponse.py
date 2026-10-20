from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app=FastAPI()

#1. 클라이언트가 /resp/3?msg=hello 요청
#2. resp함수 실행
#3. 함수가 json응답을 만들어 반환
#4. 클라이언트는 상태코드200과 json 데이터 받음


@app.get("/resp/{stu_id}", response_class=JSONResponse)
def resp(stu_id:int, msg:str|None=None):
    return JSONResponse(content={
        'con':'fastapi',
        'stu_id':stu_id,
        'msg':msg
    }, status_code=status.HTTP_200_OK)


