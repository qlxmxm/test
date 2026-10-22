from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError


#데이터베이스 connection url
#            db유형+드라이버명://사용자명:비번@localhost:포트번호/db명

DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw"

#엔진 생성
#sqlalchemy에서 데이터베이스 연결 객체를 생성하는 함수
#poolclass=QueuePool : 매번 DB연결 객체 생성안하고 미리 연결 만들어서 재사용하려고(성능 up, 속도 up)
engine=create_engine(DATABASE_CONN, poolclass=QueuePool)

try:
    #엔진으로부터 연결객체를 얻는다
    conn=engine.connect()
    #sql요청
    query="select stu_no, stu_name from student"
    #문자열로 작성된 sql을 실행가능한 sql문 객체로 감싸준다
    stmt=text(query)

    #sql실행하고 CursorResult반환 -> 쿼리문 결과 result에 저장
    result=conn.execute(stmt)
    print(result)

    #결과 행을 리스트로 가져옴
    rows=result.fetchall()
    print(rows)

except SQLAlchemyError as e:
    print(e)


finally:
    conn.close()  #연결객체 반환