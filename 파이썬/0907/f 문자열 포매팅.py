#f 문자열  포매팅

#p.71
name='홍길동'
age=30
str1=f'내 이름은 {name} 입니다. 나이는 {age} 입니다'
print(str1)

name2='홍길동'
age2=20
str2='내 이름은 {0}입니다. 나이는 {1} 입니다.'.format(name2, age2)

x=10
y=30
z='Lee'

#c스타일(서식문자)
test1='z=%s, sum=%d' %(z, (x+y))
print(test1)

#format함수
#p.68
test2='z={z}, sum={sum}'.format(z=z,sum=x+y)
print(test2)

test3=f'z={z}, sum={x+y}'
print(test3)

#정렬
print(f"{'hello':_<10}")
print(f"{'hello':_^10}")

n=50
print(f"{n:_^10}")

#20개 자리수 왼쪽정렬 , 10개 자리수 오른쪽 정렬
print(f"{n:_<20}")
print(f"{n:_>10}")

#10개 자리수 확보하고 n을 출력하는데, 공백을 -로 채우기(왼쪽정렬로)
print(f"{n:_<10}")

#20개 자리수 확보하고 n을 출력하는데, 공백을 -로 채우기(오른쪽정렬로)
print(f"{n:_>20}")







