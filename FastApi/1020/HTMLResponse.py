from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

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