from datetime import date

class Diary:
    def __init__(self, filename="diary.txt"):
        self.filename=filename

    def write(self,content):
        today=date.today()
        #diary.txt를 a모드로 설정해서 content를 파일에 저장
        with open(self.filename,"a",encoding="utf-8") as f:
            f.write(f"{today} : {content}\n")


    #파일에 저장한 문장들을 읽어온다.
    def read_all(self):
        try:
            with open(self.filename,"r",encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("파일이없어 일기 못읽어옴")            


diary=Diary()
diary.write("파이썬 복습해야지")
diary.write("파이썬 오늘 정리함")
diary.read_all()