# /members?name=홍길동
# → {"name": "홍길동", "age": null}
# /members?age=25
# → {"name": null, "age": 25}
# /members?name=철수&age=30
# → {"name": "철수", "age": 30}

from fastapi import FastAPI

app=FastAPI()

@app.get('/members')
def test(name:str | None=None,age:int | None=None):
    return {'name':name, 'age':age}