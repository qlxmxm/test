from fastapi import FastAPI, Form, status
from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from decimal import Decimal

app=FastAPI()

class Num(BaseModel):
    positive:int=Field(gt=0)  #0보다 커야함
    non_positive:int=Field(ge=0) #0이상이어야함
    negative:int=Field(lt=0) #0보다 작아야함
    non_nega:int=Field(le=0) #0이하이어야함
    even:int=Field(multiple_of=2) #2의 배수
    #2진수로 저장 :float 1/3=>0.333333333(16개)
    pydan:float=Field(allow_inf_nan=True) #무한대 /NaN허용

    short:str=Field(min_length=3)
    long:str=Field(max_length=10)
    rege:str=Field(pattern=r'^\d*$') #0개이상의 숫자(0-9)
    # 10진수로 저장 : Decimal 1/3=> 0.33333333333333333333333 (28자리)

    f1:Decimal=Field(max_digits=5,decimal_places=2) #최대자리수 5자리, 소수점이하 최대 2자리



num=Num(positive=1, non_positive=0, negative=-2, non_nega=0, even=2, pydan=float('inf'),
        short='aaa', long='ee', rege='123', f1=333.3)


print(num)