from passlib.context import CryptContext
import jwt
import uuid
from datetime import datetime, timedelta, timezone
from app.core.setting import settings

#사용할 해시 알고리즘 지정
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")


#db에 비밀번호를 그대로 저장-> db유출되면 비밀번호 다 노출됨..
def get_password_hash(password:str):
    #비밀번호를 utf-8로 인코딩한 후 72바이트로 자른다.
    truncate_password=password.encode('utf-8')[:72] #문자열 -> 바이트
    return pwd_context.hash(truncate_password)

#회원가입 -> 123@!!@# -> 해시 -> DB에 저장
#로그인 -> 비번입력 -> 같은 방식으로 해시 - DB에 넣은 해시랑 같냐?


def verify_password(plain_password:str, hashed_password:str)-> bool:
    truncated_pw=plain_password.encode('utf-8')[:72]
    return pwd_context.verify(truncated_pw, hashed_password) #해싱+비교


#uid: 토큰 주인(사용자 id)
#(createtoken(1, timedelta, {type="access", username="kim"}))
#헤더: 알고리즘 정보 / payload : 토큰에 담는 데이터 / 서명(서버가 만든것, 중간에 내용안바뀜(증명하는 인감역할))
def create_token(uid:int, expires_delta:timedelta, **kwargs) -> str:
    to_encode=kwargs.copy()
    expire=datetime.now(timezone.utc) + timedelta(seconds=expires_delta)
    to_encode.update({"exp":expire, "uid":uid})
    encoded_jwt=jwt.encode(to_encode, settings.secret_key, algorithm=settings.jwt_algorithm)

    return encoded_jwt


