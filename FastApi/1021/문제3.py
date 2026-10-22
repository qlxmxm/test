# /go-to-home 경로로 GET 요청을 보내면, 
# 사용자를 /home으로 리다이렉트하도록 FastAPI 코드를 작성해라
# /submit-form 경로로 POST 요청을 받으면, 
# form 데이터(username, age)를 받아서 /user-info/{username}?age={age}로 리다이렉트하도록 코드를 작성해라
# GET 요청으로 /user-info/{username}를 받으면, HTMLResponse로 사용자 이름과 나이를 보여주도록 작성해라


from fastapi import FastAPI, status, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional

app=FastAPI()

@app.get("/go-to-home", response_class=RedirectResponse)
def home():
    return RedirectResponse(url="/home")

@app.post("/submit-form", response_class=RedirectResponse)
def data(username:str=Form(), age:int=Form()):
    return RedirectResponse(url=f"/user-info/{username}?age={age}", status_code=status.HTTP_302_FOUND)

@app.get("/user-info/{username}", response_class=HTMLResponse)
def html(username:str, age:Optional[int]=None):
    content=f"""
<html>
<body>
<p>username:{username}</p>
<p>age:{age}</p>
</body>
</html>
"""
    return HTMLResponse(content=content)