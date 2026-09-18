#모듈 : 파이썬 코드 들어있는 파일 (-py 파일 하나)
#패키지 : 여러 모듈을 폴더로 묶은 것
#라이브러리 : 여러 패키지, 모듈을 모아놓은 것(ex. pandas, numpy..)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def div(x,y):
    return x/y

# print(add(4,5))
# print(sub(4,5))
# print(multi(4,5))
# print(div(4,5))

#파이썬 파일 실행할때, 파이썬 인터프리터가 자동으로 그 파일에
#__name__(이름)을 붙여준다
#직접 실행하는 파일은__name__이__main__이 되고
#다른 파일에서 import해서 사용하는 파일은 __name__이 "파일명"이 된다.
if __name__=="__main__":
    print(add(4,5))
    print(sub(4,5))
    print(multi(4,5))
    print(div(4,5))









