from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError
from db import get_conn
from datetime import datetime


def insert_article(title, author, content=None):
    with get_conn() as conn:
        if not content:
            content='비어있다'

        ch_query="select COUNT(*) from articles where title=:title and author=:author"
        result=conn.execute(text(ch_query).bindparams(title=title, author=author))
        #[(2,)]
        cnt=result.scalar() #2

        if cnt>0:
            print("이미 있는 제목과 작성자")
            return
        
        insert_sql="""
            insert into articles (title, author, content, published_at)
            values (:title, :author, :content, :published_at)
        """
        stmt=text(insert_sql).bindparams(
            title=title,
            author=author,
            content=content,
            published_at=datetime.now()
        )
        conn.execute(stmt)
        conn.commit()

def select_article(title, author):
    try:
        with get_conn() as conn:
            q="select * from articles where title=:title and author=:author"
            stmt=text(q).bindparams(title=title, author=author)
            result=conn.execute(stmt)
            rows=result.fetchall()
            for i in rows:
                print(i)
                
    except SQLAlchemyError as e:
        print(e)



# insert_article('제목1','홍길동','내용1')
# insert_article('제목2','홍길동2','내용2')
insert_article('제목3','홍길동4','내용4')
select_article('제목3','홍길동4')