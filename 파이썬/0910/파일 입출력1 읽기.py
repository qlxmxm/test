
#파일 입출력
#읽기: r, 쓰기: w(파일생성), 추가: a
#파일 읽기
#절대경로(c:\test\unit01.html), 상대경로('./, ../, ../../')
#인코딩: 문자를 숫자로 바꾸는 것
#디코딩: 숫자를 문자로 바꾸는 것
#UTF-8: 가장 많이 쓰는 국제 표준 인코딩(유니코드)
#encoding:'UTF-8'

#f=open('파일명','파일열기모드')
#쓰기
#w:쓰기(파일생성)
# f=open('./resource/news.txt','w')
# f.close()

#f=open('파일명','파일열기모드')
#1. read함수 사용
f=open('./resource/news.txt', 'r', encoding='UTF-8')
print(f)
print(f.encoding)
print(f.name)
print(f.mode)
result=f.read() #파일로부터 읽어온다
print(result)
f.close #파일 열었으면 반드시 닫기

#2. 파일객체를 for문과 사용
f=open('./resource/news.txt', 'r', encoding='UTF-8')
for i in f:
    print(i)    #줄 단위로 읽기
f.close()

#with
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    c=f.read()
    print(type(c))
    print(list(c))

print("==================================")

with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    c=f.read(30)    #채음 30문자 읽기(utf-8기준)
    print(c)

#4. readline
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    line=f.readline()   #한줄씩 출력
    print(line)
    line=f.readline()   #한줄씩 출력
    print(line)

#5. readlines
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    lines=f.readlines()
    print(lines)
    for i in lines:
        print(i)


        


