from fastapi import FastAPI, status, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/html/{stu_id}",response_class=HTMLResponse)
def html1(stu_id:int, q:str | None=None):
    content1=f"""
        <html>
                <body>
                     <h1>FastAPI</h1>
                     <p>stu_id:{stu_id}</p>
                     <p>q:{q}</p>   
                </body>
        </html>
        """
    return HTMLResponse(content=content1 , status_code=status.HTTP_200_OK)



#주소 강제이동 (get -> get) : 302상태 코드 생략가능
@app.get("/redirect")
def redirect1(msg:str|None=None):
    return RedirectResponse(url=f"/html/4?q={msg}", status_code=status.HTTP_302_FOUND)


#post->get :  상태코드 적어야함
@app.post("/redirect2")
def redirect2(stu_id:int=Form(), q:str=Form()):
    return RedirectResponse(url=f"/html/{stu_id}?q={q}", status_code=status.HTTP_302_FOUND)