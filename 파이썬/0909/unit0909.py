#1. 키를 실수로 입력받아 "너의 키는 ( ) cm이다" 라는 문자열을 출력
#format함수와 f-string사용
a=float(input("키를 입력하세요"))
#format
print("당신의 키는 {}cm 이다".format(a))
#f-string
print(f'당신의 키는 {a}cm 이다')

# 2. avg- 평균구하는 함수 구현해라.
# avg(1,2)
# avg(1,2,3,4,5) 호출코드이다.
def avg(*args):
    result=0
    for i in args:
        result+=i
    return (result/len(args))

print(avg(1,2))
print(avg(1,2,3,4,5))