class Song:
    def __init__(self,title, singer,minute):
        self.title=title
        self.singer=singer
        self.minute=minute

#Playlist클래스를 만들어 빈 리스트를 초기화하고 거기에다 song객체들을 추가한다
class Playlist:
    def __init__(self):
        self.songs=[]

    def add_song(self, song):
        self.songs.append(song)

    def total_minute(self):
        #self.songs=[s1,s2,s3]
        return sum(i.minute for i in self.songs)

    def long_song(self):
        minutes=[i.minute for i in self.songs] #[3,3,4]
        max_minute=max(minutes)

        for i in self.songs:
            if i.minute == max_minute:
                return i.title


p1=Playlist()
p1.add_song(Song("Love attack","리센느",3))
p1.add_song(Song("갑자기","아이오아이",3))
p1.add_song(Song("Dynamite","BTS",4))

print("전체 재생시간 :", p1.total_minute() , "분")
print("가장 긴 곡 :" , p1.long_song())