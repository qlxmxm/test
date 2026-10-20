from fastapi import FastAPI, Request
from typing import Annotated

# Request 객체

# : Http Request에 대한 대부분 정보를 가지고 있다.

# request.method는 GET/POST/PUT등의 HTTP Method
# • request.url: 전체 URL
# • request.headers: Dictionary 로 제공되는 header 정보
# • request.cookies: Dictionary로 제공되는 cookie 정보
# • request.client: Client ip address/port
# • request.query_params: Dictionary 로 제공되는 query parameter
# • request.json(): request body의 json 값
# • request.form(): form data 값


app=FastAPI()

@app.get("/login")
def login(request:Request):
    client_host=request.client.host
    headers=request.headers
    query=request.query_params
    url=request.url
    path_param=request.path_params
    http_method=request.method

    return{
        "client_host":client_host,
        "headers":headers,
        "query":query,
        "url":url,
        "path_param":path_param,
        "http_method":http_method
    }