#test.py에 있는 add,multi함수 호출하고싶음
#add,multi함수가 test모듈에 있기 때문에 일단 불러와야한다

# import 패키지_모듈1

# print(패키지_모듈1.add(1,2))
# print(패키지_모듈1.multi(1,2))

# from 패키지_모듈1 import add,multi
# print(add(1,2))
# print(multi(1,2))

from 패키지_모듈1 import *
print(add(1,2))
print(multi(1,2))





