#호출하면 바로 실행되고, 끝날때까지 멈추지 않는다.
# def func():
#     print("hi")
#     return 1

# result=func()
# print(result)

# #코루틴 함수(async def로 정의)
# import asyncio

# async def main():
#     print('Hello...')
#     await asyncio.sleep(1)
#     print('...World!')

# asyncio.run(main())

import asyncio

#코루틴(coroutine)
async def show(name, sec):  #비동기함수
    print("start")
    await asyncio.sleep(sec)    #다른 비동기 작업이 끝날때까지 기다림
    print("final")

async def main():
    #show 2개 코루틴을 동시에 실행시켜줘. 그리고 둘 다 끝날때까지 기다려줘.
    await asyncio.gather(
        show('python',2),
        show('java',3)
    )

asyncio.run(main())

#1. main 함수 실행 -> show함수 동시에 실행
#2. 2초동안 python작업이 완료됨
# 동기식이면 5초걸리는데 , 비동기 방식으로 해서 3초걸림






