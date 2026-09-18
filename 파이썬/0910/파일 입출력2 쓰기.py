
#쓰기
#w:쓰기(파일생성)

with open('./resource/test1.txt', 'w') as f: #test1.txt 파일을생성하여
    f.write('hi python!!\n')    #test1.txt파일에 문자열쓰기(저장)

with open('./resource/test1.txt', 'w') as f:
    f.write("hi react!!\n") #문자열 append (덮여쓰기)

#줄바꿈 : writelines
with open('./resource/test2.txt', 'w') as f:
    li=['React\n','DB\n','Python\n']
    f.writelines(li)






