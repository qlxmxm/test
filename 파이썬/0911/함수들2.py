#p.258
#time:시간관련처리
import time
print(time.time())

print(time.localtime(time.time()))

#현재시간 리턴
print(time.ctime())

#포멧코드(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(time.time())))

#random:난수리턴
import random

print(random.random())  #0.0 이상 ~ 1.0 실수

print(random.randint(1,45)) #1~45포함 정수

#섞기
d=[1,2,3,4,5]
random.shuffle(d)
print(d)

#무작위 선택
c=random.choice(d)
print(c)

#p.273
#**pickle:객체 파일 쓰기**
import pickle
f=open('test.obj','wb') #파일을 쓰기용 바이너리 모드로 열기
obj={1:'python',2:'study',3:'basic'}
pickle.dump(obj,f)  #객체를 파일에 저장(직렬화)
f.close()

#with open('test.obj','wb') as f:
#   pickle.dump(obj,f)

with open('test.obj','rb') as f:
    data=pickle.load(f)
print(data)

"""
#p.286
import webbrowser
webbrowser.open('http://google.com')
webbrowser.open_new('http://google.com')
"""







