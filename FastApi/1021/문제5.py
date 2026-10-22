# FastAPI 앱에서 /plaintext 경로를 만든다
# 해당 경로는 GET 요청을 받고,
# 응답으로 "Hello, World!"를 plain text 형식으로 반환해야 한다
# FastAPI의 ResponseClass를 활용하여 응답 타입을 PlainTextResponse로 지정한다
# /json 경로는 GET 요청을 받고,
# JSON으로 { "message": "Hello, JSON!" }를 반환해라.

from fastapi import FastAPI, status, Form
from fastapi.responses import RedirectResponse, HTMLResponse, PlainTextResponse
from pydantic import BaseModel
from typing import Optional
import json

app=FastAPI()

@app.get("/plaintext", response_class=PlainTextResponse)
def hi():
    return PlainTextResponse("HelloWorld")

@app.get("/json")
def json():
    return { "message": "Hello, JSON!" }