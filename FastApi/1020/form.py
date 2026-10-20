from fastapi import FastAPI, Form
from typing import Annotated

app=FastAPI()

@app.post("/login")
def login(
    username:str=Form(),
    email:str=Form(None),
    addr:Annotated[str, Form()]=None
    ):

    return {"username":username,
            "email":email,
            "addr":addr
            }

@app.post("/login2")
def login2(username:str=Form(...),
           email:str=Form(...),
           addr:str=Form(...),
           ):

        return {"username":username,
            "email":email,
            "addr":addr
            }










