#ex 음식점알바..
#주문,요리,서빙까지 순서대로 한명씩 처리 -> 줄서서기다림

#스러드 vs 비동기의 차이점
#여러파일을 동시에 다운로드 vs 다운로드 도중 다른 작업처리
#직원을 여러명 고용 vs 직원1명이 요리하는 동안 다른일을 처리
#cpu많이 쓰고 독립적으로 여러작업 vs 기다리는 시간이 많은작업

import threading
import time

def game(name,sec):
    print(f"{name}입장")
    time.sleep(2)
    print(f"{name}퇴장")

#스레드 객체생성
#Thread : 파이썬 제공 클래스 -> threading 모듈에 정의되었다.
t1=threading.Thread(target=game,args=("음악",2))
t2=threading.Thread(target=game,args=("채팅",3))

#스레드 시작메소드 -> target걸었던 함수호출
t1.start() #game()
t2.start() 


# import threading
# import time

# def game(name):
#     print(f"{name}입장")
#     time.sleep(2)
#     print(f"{name}퇴장")
# name=["음악","채팅","게임"]

# threads=[]

# for i in name:
#     #반복문안에서 "음악","채팅", "게임" -> 각각 스레드로 만듬
#     t=threading.Thread(target=game, args=(i,))
#     t.start()   #쓰레드 실행 메소드
#     threads.append(t)

# for t in threads:
#     print(t)
#     t.join()    #모든 작업 스레드 다 끝날때까지 대기
#     #스레드 자제가 비동기적으로 실행되므로, 다른 스레드의 작업완료를 기다리지않고 먼저 끝나버릴수가 있기 때문에 적어야함

# #1. 3개 스레드 동시시작
# #2. target으로 설정한 game메소드가 실행됨
# #   2초동안 기다린 후 3개 스레드가 동시에 종료됨

# # start 를 먼저 실행시킨다고 해서 먼저 실행되는것은 아님 -> 실제로 어떤 스레드가 몇번째로 실행할지는 모름(os의 스케쥴러가 결정함)


