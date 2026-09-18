""" Escap 코드
\n 개행 (enter)
\t 탭   (tab)
\\ 문자 (\안녕)
\'      (문자열이 작은따옴표로 감싸져있을때- 내우에 '를 넣고 싶을때)
\''
\000    (\뒤에 8진수 숫자를 붙여 해당 아스키를 문자로 표현)
"""

print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print("It\'s me")
print("He saild \"hi\"")
print("\000")

#문자열 출력
print('Python Welcome')
print("Python Welcome")
print("""Python Welcome
        wel
        come""")
print('''s'Python Welcome
        wel
        come''')

food="python's favorite food is per1"
print(food)
say='"Python is very easy" he says'
print(say)
say1="'Python is very easy' he says"
print(say1)

str1="Python interesting"
print(str1[7])
print(len(str1))        #18

print(str1[0:3])        #0~2까지 추출 #Pyt
print(str1[:])          #Python interesting
print(str1[:4])         #Pyth 출력
print(str1[4:])         #인덱스 4부터 끝까지
print(str1[:len(str1)]) #인덱스 0부터 문자열의 길이-1
print(str1[1:-2])       #인덱스 1부터 뒤에서 3번째까지
print(str1[-4:-2])      #뒤에서 4번쨰부터 3번쨰
print(str1[1:18:2])     #인데스 1부터 3까지 2칸씩 점프








