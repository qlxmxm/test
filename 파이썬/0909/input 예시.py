#초기값 설정
def say(name,man,old=20):
    print(name)
    if man:
        print('남자', old)
    else:
        print('여자', old)

say('juli', True)
say('tom', False, 10)

#p.171
a=input("너는 뭘 좋아해?")
print(a)

# a=input("키 몇 cm")
# print(a)

# a=int(input('정수 하나입력'))
# b=int(input('정수 하나입력'))
# print(a+b)

a=int(input('정수 하나입력'))
b=int(input('정수 하나입력'))
print(a*b)

a=float(input("키 몇 cm?"))
print(a)






