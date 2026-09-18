#문제2.
# 나이 입력 프로그램
# 사용자에게 나이 입력 받기
# 숫자가 아니면 예외 처리
# (0 이하 입력하면 사용자 정의 예외 발생)
# 정상 입력 시 "입력 완료"

class AgeError(Exception):
    def __init__(self):
        super().__init__('0보다 커야해')

try:
    age=int(input('나이 입력'))

    if(age<=0):
        raise AgeError('나이는 0이상이어야해')
    print("입력 완료")

except AgeError as e:
    print(e)

except ValueError as e:
    print(e)
    print("숫자 입력해야되!")










