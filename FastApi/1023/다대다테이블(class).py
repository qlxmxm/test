from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy import String, ForeignKey,create_engine


DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw1"
engine=create_engine(DATABASE_CONN)

#SessionLocal은 세션자체가 아니라 세션을 만들어 주는 공장
SessionLocal=sessionmaker(bind=engine)


def get_db():
    db=SessionLocal()  #새로운 session객체 생성
    try:
        yield db
    finally:
        db.close()



# Base는 sqlalchemy에서 가져오는 게 아니라 직접 만드는 클래스
class Base(DeclarativeBase):
    pass

# 한 노래는 여러 플레이리스트에 들어갈 수 있고
# 한 플레이리스트에는 여러 노래가 들어감
class SongPlaylist(Base):
    __tablename__="songplaylists"

    song_id:Mapped[int]=mapped_column(ForeignKey("song.id"), primary_key=True)
    playlist_id:Mapped[int]=mapped_column(ForeignKey("playlists.id"), primary_key=True)

    #SongPlaylist 는 Song 하나를 가르킴(단수) -> 그 Song에서 부르는 이름: playlists
    song:Mapped["Song"]=relationship(back_populates="playlists")
    #SongPlaylist 는 Playlist 하나를 가르킴(단수) -> 그 Playlist에서 부르는 이름: songs
    playlist:Mapped["Playlist"]=relationship(back_populates="songs")

class Song(Base):
    __tablename__="songs"
    #primary_key 이고 + 정수형 -> 자동으로 auto_increment 적용됨
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(50))

    playlists:Mapped[list["SongPlaylist"]]=relationship(back_populates="song")
    

class Playlist(Base):
    __tablename__="playlists"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(50))
    
    songs:Mapped[list["SongPlaylist"]]=relationship(back_populates="playlist")


Base.metadata.create_all(bind=engine)