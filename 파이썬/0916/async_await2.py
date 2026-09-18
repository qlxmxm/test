# #코루틴 함수(async def로 정의)
import asyncio

async def say_hello():
    print("안녕!")
    await asyncio.sleep(2)  #await- 비동기 함수 안에서 다른 비동기 함수를 호출할 때 사용
    print("2초 뒤에 또 안녕!")

async def main():
    await say_hello()

#asyncio로 비동기 함수 실행
asyncio.run(main()) #비동기 함수 시작