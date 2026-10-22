from fastapi import FastAPI, Form, status
from pydantic import BaseModel
from typing import Optional
import json
from fastapi.responses import RedirectResponse, HTMLResponse, PlainTextResponse
from start.routes import item



app=FastAPI()

#item.py에 있는 router객체
app.include_router(item.router)