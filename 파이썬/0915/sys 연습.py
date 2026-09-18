#p.147
def gugu(n):
    result=[]
    i=1
    while i<10:
        result.append(n*i)
        i=i+1
    return result

print(gugu(2))

result=[i*2 for i in range(1,10)]
print(result)

#sys : 실행 관련 제어
import sys
print(sys)
print(sys.path)
print(type(sys.path))

print("start")
sys.exit()  #프로그램 즉시 종료
print('end')



