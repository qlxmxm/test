#format - c스타일(%s:문자열, %f:실수, %d:정수)
print('문자열 %s와 문자열 %s가 있다' %('one','two'))
print("%d %d" %(3,4))
print("%f %f" %(3.14,7.92))     #%f는 소수6자리 기준
print("%.3f %.2f" %(3.14,7.92))

#p.66
print("%10s" %("hi"))   #10자리에서 오른쪽으로 정렬로 hi출력됨
print("%-10s" %("hi") + "bye")   #10자리에서 왼쪽으로 정렬로 hi출력됨

#정수 4,6을 입력 -> %d로
print("%d %d" %(4,6))
#python이라는 문자를 20자리에서 오른쪽 정렬로 출력
print("%20s" %("python"))

#format함수
print("I eat {0} apples".format(3))

print("{} {}".format('one','two'))

print("{1} {0}".format('one','two'))

print("{0} {1}".format(1,2))

#c스타일로 10자리에서 오른쪽정렬로 python출력
print("%10s" %("python"))
print("{:>10}".format('python'))
print("%-10s" %('python') + "hi")

#5자리까지 출력(절삭)
print("%.5s" %('pythonjavascipt'))

print("%6.2f" %(3.14159212345667)) #총 6개에서 소수점은 2자리 [6자리공간에 소수점 2자리까지 표시, 숫자가 부족하면 앞에 공백으로 자리 채움]

print("%06.2f" %(3.14159212345667)) #총 6개에서 소수점은 2자리/ 앞부분으로 0으로 채워라

x=30
y=50
z=42032
str="kim"

ex1='%s %f %d' %(str, z, (x+y))
print(ex1)
print(type(z))

print("{0:<10}".format('hi') + "bye")
print("{0:>10}".format('hi') + "bye")
print("{0:^10}".format('hi') + "bye")

#20자리 "script" 출력 오른쪽정렬
#서식문자, format
print("%20s" %('script'))
print("{0:>20}".format('script'))

#왼쪽정렬 10자리 바꾸지
#서식문자, format
print("%-10s" %('script'))
print("{0:<10}".format('script'))

#10자리 "python" 왼쪽정렬(자리남으면 _로 채워라)
print("{:_<10}".format('python'))

#python 문자 10자리 중앙정렬
print("{0:_^10}".format('python'))













