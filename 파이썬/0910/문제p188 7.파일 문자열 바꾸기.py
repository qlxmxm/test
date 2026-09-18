#p187 7.다음과 같은 내용을 자닌 test.txt가 있다. 이 파일의 내용 중
#"java"라는 문자열을 "python"으로 바꾸어 저장해 보자.

#Life is too short
#you need java

f=open('test.txt', 'r',encoding='UTF-8')
body=f.read() #test.txt의 내용을 body 변수에 저장
f.close()
body=body.replace("java","python")  #body문자열에서 "java"를 "python으로 변경"
f=open('test.txt', 'w',encoding='UTF-8')    #파일을 쓰기 모드로 다시 실행
f.write(body)
f.close()
