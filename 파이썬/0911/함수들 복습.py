#내장 함수(자주 사용하는 함수 위주)
#p.242 절댓값
print(abs(-3))

#all,any : iterable 요소 검사(참,거짓)
print(all([1,2,3])) #and
print(all([1,2,0]))

print(any([1,2,0])) #or(하나라도 참인 요소 있으면 true)

print("==================================")

a=[60,1,4,10,50]
#if all(i<20 for i in a): #리스트 안에 있는 값이 다 20보다 작아야 true
if any(i>30 for i in a): #리스트 안에 있는 값이 30보다 큰게 하나만 있으면 true
    print("ok")
else:
    print("cancel")

print("==================================")

#chr : 아스키 -> 문자, ord: 문자 -> 아스키
print(chr(65))
print(ord("A"))

print("==================================")

#enumerate : 인덱스 + iterable 객체
for i,name in enumerate(['body','foo','bar']):
    print(i,name)

print("==================================")

#filter : 반복가능한 객체 요소를 지정한 후 조건에 맞는 값 추출
def num(x):
    return abs(x)>3

print(list(filter(num,[-3,2,4,-4,-10,-100])))
#lambda로 바꾸기
print(list(filter(lambda x:abs(x)>3,[-3,2,4,-4,-10,-100])))

#id:객체의 주소값 반환
print(id(int(10)))
print(id(10))
print(id(11))

#len:길이반환
print(len('python'))
print(len([1,2,3,4,5]))

#p.250
#map:반복가능한 객체 요소를 지정한 함수 실행 후 추출
#반복가능한 객체:리스트,튜플,문자열,딕셔너리,range,파일객체....
def num2(x):
    return x
#map(함수명넣어서)
print(list(map(num2,[-3,2,4,-4,-10,100])))
#map(lambda)
print(list(map(lambda x:x, [-3,2,4,-4,-10,100])))

#range:반환가능한 객체 반환
print(range(5)) #끝 숫자만 지정
print(range(1,10,2))
print(list(range(1,10,2)))
#0~-9 까지 -1씩 감소시키면서 리스트로 출력
print(list(range(0,-10,-1)))

for i in range(5):
    print(i)

#p.251
#max,min 최대,최소
print(max([1,2,3]))
print(max("python"))    #사전순 제일 마지막에 있는 문자
print(min(1,2,3))
print(min("python"))    #사전순 제일 앞에 있는 문자
print(max((1,2,3)))

#round:반올림
print(round(4.6))
print(round(3.6432,2))  #소수점 둘째자리까지

#sorted:반복가능한 객체 정렬 후 반환
print(sorted([5,6,2,1,2,4]))
a=sorted([5,6,2,1,2,4])
print(a)
print(sorted(['p','y','t','h','o','n']))

#sum:반복가능한 객체 합 반환
print(sum([1,2,3,4,5]))
print(sum(range(1,101)))

#type:자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))

#p.255
#zip:반복가능한 객체의 요소 묶어서 반환(인덱스 순서대로 묶임)
print(list(zip([10,20,30],[40,50,60])))
print(type(list(zip([10,20,30],[40,50,60]))))






