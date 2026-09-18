# 무한대로 짝수를 생성해라
# g = even_gen()
# print(next(g)) #0
# print(next(g)) #2
# print(next(g)) #4

# # 제너레이터
# def even_gen():
#     num=0
#     while True:
#         yield num
#         num +=2

# g = even_gen()
# print(next(g)) #0
# print(next(g)) #2
# print(next(g)) #4

print("===============================")

#이터레이터
class even_gen:
    def __init__(self):
        self.n=0

    def __iter__(self):  #iter(Cnt(5)) -> 이터레이터 객체 만듬
        return self

    def __next__(self):  #next(obj) -> 반환된 이터레이터 객체에 next()반복호출
        result=self.n
        self.n+=2
        return result

g = even_gen() #이터레이터 객체 생성
print(next(g)) #0
print(next(g)) #2
print(next(g)) #4