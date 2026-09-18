#계산기 함수 만들기
# calc("add", 1,2,3) # 6
# calc("mul", 1,2,3,4) # 24
# calc("avg", 10,20,30) # 20

# 가변 인자 사용
# 잘못된 연산이면 예외 발생
def calc(oper, *args):
    try:
        if oper=='add':
            return sum(args)

        elif oper=='mul':
            multi = 1
            for n in args:
                multi *= n
            return multi

        elif oper=='avg':
            return sum(args)/len(args)

        else:
            raise ValueError('잘못된 연산이다')
            #예외를 일부터 발생시켜보기

    except ValueError as e:
        print(e)

print(calc("add", 1,2,3))
print(calc("mul", 1,2,3,4))
print(calc("avg", 10,20,30))
print(calc("abc", 5,7,9))



