#사용자 정의 예외 -> 우리가 만드는 예외 -> Exception클래스를 상속받아서 만든다.
class ShortPassword(Exception):
    def __init__(self):
        super().__init__("비밀번호는 4자 이상이어야 합니다")

class NoDigit(Exception):
    def __init__(self):
        super().__init__("비밀번호에 숫자가 최소 1개는 포함되어야 합니다")


def check_pw():
    pw=input("비밀번호 입력하세요")
    try:
        if len(pw) < 4:
            raise ShortPassword()
        
        if not any(i.isdigit() for i in pw):
            raise NoDigit()

    except (ShortPassword,NoDigit) as e:
        print(e)

check_pw()