# #1.문자열 바꾸기
# #다음과 같은 문자열을 split과 join 함수를 사용하여 고치시오
# # a:b:c:d ==> a#b#c#
# result = "a:b:c:d"

# a = result.split(':')

# b = '#'.join(a)

# print(a)
# print(b)

# #2.딕셔너리 값 추출하기 
# #다음은 딕셔너리 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다
# # >>>a={'A':90, 'B':80}
# # >>>a['C']

# # Traceback (most recent call last):
# #   File "c:\jw-git\파이썬\0918\unit0916.py", line 19, in <module>
# #     print(a['C'])
# # KeyError: 'C'

# #a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다.
# #'C'에 해당하는 key 값이 없을경우, 오류 대신 70을 얻을 수 있도록 수정하시오.

# a={'A':90, 'B':80}
# try: 
#     print(a['C'])
# except Exception as e: 
#     a['C']=70
#     print(a['C'])
    
#3.리스트의 더하기와 extend 함수
#리스트 a에 [4,5]를 + 를 사용한 것과 extend를 사용한 차이점은 무엇인가?
# a=[1,2,3]
# print(id(a))    #2200166127040
# a=a+[4,5]

# print(a) #[1,2,3,4,5]
# print(id(a))    #2672658114176

# a=[1,2,3]
# print(id(a))    #2082937165248
# a.extend([4,5]) 

# print(a) #[1,2,3,4,5]
# print(id(a))    #2082937165248

#+는 새로운 리스트를 만드는 거고 extend는 기존거에 합친것이다.(id차이)

#4.리스트 총합 구하기
#다음은 A학급 학생의 점수를 나타내는 리스트이다.
#다음 리스트에서 50점 이상 점수의 총합을 구하시오.

# A=[20,55,67,82,45,33,90,87,100,25]

# sum=0

# for score in A:
#     if score>=50:
#         sum+=score

# print(sum)
    
#5.피보나치 함수
#첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때 이후에 이어지는
#항은 이전의 두항을 더한 값으로 이루어지는 수열을 '피보나치 수열'이라고한다.
#0,1,1,2,3,5,8,13........
#입력을 정수 n으로 받았을 때 n항 이 하까지의 파보나치 수열을 출력하는 함수를 작성하시오.

# def number(n):
#     a, b = 0, 1
    
#     result = []
    
#     while len(result) <= n-1:
#         result.append(a)
#         a, b = b, a + b
        
#     print(result)

# num = int(input("몇항까지 출력할지 입력하세요 : "))

# number(num)

#6.숫자의 총합 구하기
#사용자에게 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을
#구하는 프로그램을 작성하시오.(단, 숫자는','로 구분하여 입력한다)
#65,45,2,3,45,8

# num = input(",로 숫자들을 입력하시오")

# a = num.split(',')

# sum=0

# for total_sum in a:
#     sum+=int(total_sum)

# print(sum)

#7.한 줄 구구단
#사용자에게 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을
#한 줄로 출력하는 프로그램을 작성하시오

# a=int(input("구구단을 출력할 숫자를 입력하세요(2~9) : "))

# if a<2 or a>=10:
#     print("2~9 사이 숫자만 입력하세요")
# else:
#     for i in range(1,10):
#         print(a*i, end=" ")

#8. 파일을 읽어서 역순으로 저장하기
#다음과 같은 내용의 파일 abc.txt가 있다. (a,b,c,d,e)
#이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오

# with open("abc.txt", "r") as f:
#     lines = f.readlines()

# lines.reverse()

# with open("abc.txt", "w") as f:
#     for line in lines:
#         f.write(line)

#9.평균값 구하기
#다음과 같이 총 10줄로 이루어진 sample.txt가 있다. sample.txt의 숫자 값을
#모두 읽어 총합과 평균값을 구한 후 평균값을 result.txt에 쓰는 프로그램을 작성하시오

# f= open("sample.txt") 
# lines = f.readlines()
# f.close()

# total = 0
# for line in lines:
#     score = int(line)
#     total += score
# average = total / len(lines)

# f= open("result.txt", "w") 
# f.write(str(average)) 
# f.close()

#10. 계산기 만들기
#다음과 같이 동작하는 클래스 Calculator를 작성하시오
#cal1 = Calculator([1,2,3,4,5])
#cal1.sum() #합
#cal1.avg() #평균
#cal2 = Calculator([6,7,8,9,10])
#cal2.sum()
#cal2.avg()
# class Calculator:
#     def __init__(self, num_list):
#         self.num_list = num_list

#     def sum(self):
#         return sum(self.num_list)

#     def avg(self):
            
#         return sum(self.num_list) / len(self.num_list)

# cal1 = Calculator([1, 2, 3, 4, 5])
# print(cal1.sum())  # 15
# print(cal1.avg())  # 3.0

# cal2 = Calculator([6, 7, 8, 9, 10])
# print(cal2.sum())  # 40
# print(cal2.avg())  # 8.0

#11.모듈을 사용하는 방법
#C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해보자. 
#명령 프롬프트 창에서 파이썬 셸을 열어 이 모듈을 impot해서 사용할 수
#있는 방법을 모두 기술하시오(즉, 다음과 같이 import mymod를 수행할 때 오류가 없어야 한다).
#import mymod
# <--- 오류 없음

# import sys
# sys.path.append("c:/doit")
# import mymod

#12.오류와 예외처리
#다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.

# result = 0

# try:
#     [1,2,3][3]  #[1,2,3]의 인덱스가 0~2 까지인데 [3] 인덱스를 불러와서 IndexError 에러
#     "a" + 1 #"a" 문자에 정수 1을 더화라고 해서 TypeError 에러
#     4 / 0   #0나누기 에러 ZeroDivisionError
# except TypeError:   #타입오류
#     result +=1
# except ZeroDivisionError:   #0나누기 에러 ZeroDivisionError
#     result +=2
# except IndexError:  #인덱스 에러
#     result +=3
# finally:
#     result +=4

# print(result)

#결과는 : 7 => [1,2,3][3] 먼저 인덱스 에러가 나와 result +=3 후 finally: result +=4가 실해되서 3+4=7

#13.
# Dashinsert 함수
# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 
# 두 수 사이에 '_'를추가하고 짝수가 연속되면 '*'를 추가하는 기능을 가지고 있다. 
# Dashinsert함수를 완성하시오

# 입력 예시: 4546793 
# 출력 예시: 454*67-9-3

# data = "4546793" 
# numbers = list(map(int, data)) 
# result=[]
# for i, num in enumerate(numbers):   #enumerate(numbers) 값과 순서번호(i,인덱스)를 동시에 꺼내줌
#     result.append(str(num)) 
#     if i < len(numbers)-1: 
#         is_odd = num %2 ==1 
#         is_next_odd = numbers[i+1] % 2 ==1  #numbers[i+1] 현제 숫자 바로 뒷 숫자
#         if is_odd and is_next_odd: 
#             result.append("-") 
#         elif not is_odd and not is_next_odd: 
#             result.append("*")

# print("".join(result))

#14
# 문자열 압축하기 
# 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우, 
# 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.

# 입력 예시: aaabbcccccca 
# 출력 예시: a3b2c6a1

# def compress_string(s):
#     _c = "" # 직전 문자를 기억할 변수(처음에는 비교대상이 없으므로 빈 문자열)
#     cnt = 0        
#     result = ""    
    
#     for c in s:
#         if c != _c:                  
#             _c = c                   
#             if cnt: result += str(cnt)  #이전 글자의 최종 개수를 숫자로 채워 넣음 (단, 처음 시작할 땐 cnt가 0이므로 패스)
#             result += _c
#             cnt = 1                  
#         else:                        
#             cnt += 1                 
            
#     if cnt: result += str(cnt)  #마지막 글자에 숫자 붙여주기
#     return result

# print(compress_string("aaabbcccccca"))  

#15
# Duplicate Numbers 함수 
# 0~9의 문자로 된 숫자를 입력받았을 때 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 
# 사용한 것인지 확인하는 함수를 작성하시오

# 입력 예시: 0123456789 01234 01234567890 6789012345 012322456789 
# 출력 예시: True False False True False

# def chk_dup_numbers(s): 
#     result = [] 
#     for num in s:
#         if num not in result: 
#             result.append(num)
#         else:
#             return False 
        
#     return len(result) == 10
        
# print(chk_dup_numbers("0123456789"))
# # True 리턴
# print(chk_dup_numbers("01234"))
# # False 리턴
# print(chk_dup_numbers("01234567890"))
# # False 리턴
# print(chk_dup_numbers("6789012345"))
# # True 리턴
# print(chk_dup_numbers("012322456789"))
# # False 리턴

