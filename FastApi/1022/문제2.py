# 경로 변수 item_id는 1 이상만 허용
# 쿼리 변수 q는 최대 길이 10
# 잘못된 값이 들어오면 (FastAPI가 422 응답 반환 )- 유효하지 않으면 에러 발생
# - get("/items/{item_id}")로 요청 -> item_id, q - json으로 받기

	
# 문제 2(총정리) - Path, Query 검증 API댓글수

from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field,EmailStr,model_validator,field_validator,ValidationError

app=FastAPI()

@app.get("/items/{item_id}")
def item(item_id:int=Path(ge=1),
q:str|None=Query(None,max_length=10)):
    return {"item_id" : item_id, "q" : q}