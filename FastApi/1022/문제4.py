# Student 모델 정의: name, score, stu_id (str, int, int)
# score보다 stu_id 더 크면 오류 발생
# model_validator를 활용할 것 


from fastapi import FastAPI,Form
from pydantic import BaseModel,model_validator,ValidationError,Field
app=FastAPI()

class Student(BaseModel):
    name:str=Field(...)
    score:int=Field(...)
    stu_id:int=Field(...)

    @model_validator(mode='before')
    @classmethod
    def test1(cls,val):
        name=val.get('name')
        score=val.get('score')
        stu_id=val.get('stu_id')

        if score<stu_id:
            raise ValueError ('학번이 점수보다 낮아야 함')
        return val


@app.post('/student')
async def cr_stu(student:Student):
    return student
