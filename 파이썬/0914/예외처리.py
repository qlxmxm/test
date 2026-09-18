#예외처리
#SyntaxError, NameError, IndexError, ZeroDivisionError, KeyError, ValueError, TypeError....

#print('h)
#print('hi'))

# x=3
# y=4
# print(z)

# a=[1,2,3]
# print(a[5])

#print(4/0)

# a={'a':'gg','b':33}
# print(a['b'])
# print(a['c'])

# x=[1,2,3]
# x.remove(2)
# x.remove(5) #ValueError

# f=open('b.txt','r')

# x=[1,2]
# y='python'
# #print(x+y) #TypeError
# print(x+list(y))

# li=['db','python','react']
# try: #예외가 날 수도 있는 코드블럭
#     x='java'
#     y=li.index(x) #예외발생 하자마자 except절로 넘어감
#     print('try 블럭 수행')

# except ValueError: #예외 발생할때 실행되는 블럭
#     print('except 블럭 수행')

# else: #예외 없을때 실행되는 블럭
#     print('else')


li=['db','python','react']
try: #예외가 날 수도 있는 코드블럭
    x='java'
    y=li.index(x) #예외발생 하자마자 except절로 넘어감
    print('try 블럭 수행')

except Exception as e: #예외 발생할때 실행되는 블럭
    print(e)

else: #예외 없을때 실행되는 블럭
    print('else')

finally: #무조건 실행되는 블럭(예외발생여부 상관없음)
    print('finally')



# class MyError(Exception):
#     def __str__(self):
#         return "허용되지 않는 별명입니다."
# def say_nick(nick):
#     if nick=='바보':
#         raise MyError()
#     print(nick)

# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError as e:
#     print(e)


#__call__: 객체를 함수형태로 쓸수있음
# mul3=Mul(3)
# mul3(10) -> 10을 __call__ 메소드 자동호출 -> 10을 __call__(n)에 전달하고있음