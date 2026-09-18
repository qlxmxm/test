#메모리 효율성
#상태 유지가 자동으로 됨(별도로 변수를 관리할 필요 없음)

#generator : 이터레이터 생성해주는 함수(yield 키워드)
#발생자 -> 메모리 절약, 속도 효율성, 문법 간결
# __iter__, __next__없이 yield만으로 이터레이터를 만들 수 있다.

#이터레이터와 제너레이터 관계는 포함관계!!!! => 제너레이터는 이터레이터의 일부분임

#값에 여러번 접근/인덱싱 필요할때/ len..,슬라이싱
#nums=[i*2 for i in range(1000000)]

#값을 한번씩만 순서대로 쓰고 버릴때/데이터가 매우 크거나 무한할때
# def get():
#     for i in range(1,1000000):
#         yield i*2

# g=get() #제너레이터 객체만 생김
# print(next(g)) #한개씩 계산되어 나옴
# print(next(g))

def gen1():
    yield 0 #0을 함수 밖에 전달하면서 코드 실행을 함수 밖에 양보함
    yield 1
    yield 2

#yield를 사용해 바깥으로 전달한 값은 next함수의 반환값으로 나온다
g1=gen1() #제너레이터 객체만 생김
a=next(g1)
print("a = ", a)

b=next(g1)
print("b = ", b)

c=next(g1)
print("c = ", c)


#새로운 제너레이터 객체를 만든다. => __iter__ , __next__ 자동으로 호출된다.
for i in gen1():
    print(i)






    