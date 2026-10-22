from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool, NullPool
from sqlalchemy.exc import SQLAlchemyError

#데이터베이스 connection url
#                DB유형 + 드라이버명
DATABASE_CONN = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw"

#엔진생성
#sqlalchemy 에서 데이터베이스 연결 객체를 생성하는 함수
#                                    기본 커넥션 풀 클래스
engine=create_engine(DATABASE_CONN, poolclass=QueuePool)

def get_conn():
    try:
        conn=engine.connect()
        return conn
    
    except SQLAlchemyError as e:
        raise e