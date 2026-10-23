from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey,create_engine


DATABASE_CONN="mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw1"
engine=create_engine(DATABASE_CONN)


# Base는 sqlalchemy에서 가져오는 게 아니라 직접 만드는 클래스
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"

    #Mapped[타입]+mapped_column
    user_id:Mapped[int]=mapped_column(primary_key=True, index=True)
    username:Mapped[str]=mapped_column(String(50), nullable=False)
    email:Mapped[str]=mapped_column(String(50), unique=True, index=True, nullable=False)


    #하나의 사용자는 여러 게시글작성가능
    #User클래스에서 posts로 Post객체 참조
    # cascade="all, delete-orphan" : user에게 한 작업(삭제, 저장) -> Post에도 적용시킴
    # all : 모든 변경사항(dml) 자식에게 전파됨
    # cascade: 부모쪽에 걸었음 -> User를 지우면 Post도 지워짐

    #posts: 사용자의 글 리스트
    posts:Mapped[list["Post"]]=relationship(back_populates="owner", cascade="all, delete-orphan")


class Post(Base):
    __tablename__="post"
    post_id:Mapped[int]=mapped_column(primary_key=True, index=True)
    title:Mapped[str]=mapped_column(String(100), nullable=False)
    content:Mapped[str]=mapped_column(String(500), nullable=False)

    #하나의 게시글은 한명의 사용자가 작성
    #Post객체에서 owner로 User객체 참조

    #owner : 게시글의 작성자 객체
    #User.posts <=> Post.owner 짝 지정 post.owner=user
    owner:Mapped["User"]=relationship(back_populates="posts")

    user_id:Mapped[int]=mapped_column(ForeignKey("users.user_id"), nullable=False)



Base.metadata.create_all(bind=engine)