#p187 5.다음은 파일(test.txt)에 "Life is too short" 문자열을 저장한 후 
# 다시 그 파일을 출력하는 프로그램이다
"""
f1=open("test.txt", 'w')
f1.write("Life is too short")

f2=open("test.txt", 'r')
print(f2.read())
""" 
#이 프로그럄은 우리가 예상한 'Life is too short' 라는 문장을
#출력하지 않는다. 우리가 예상한 값을 출력 할 수 있도록 프로그램을 수정해보자.

f1=open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2=open("test.txt", 'r')
print(f2.read())
f2.close()