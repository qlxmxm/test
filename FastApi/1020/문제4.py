from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# 도서 등록 API
# /books (POST)
# Request Body:
# { "title": "문자열(필수)", "author": "문자열(필수)", "year": "정수(선택, 기본값=2025)" }
# 응답: 등록된 도서 정보 전체 반환

app=FastAPI()

book_array = []
class Book(BaseModel):
    title: str
    author: str
    year: int = 2025

@app.post("/books")
async def create_book(book: Book):
    book_dict = book.model_dump()
    book_array.append(book_dict)
    return book_array