class AlreadyError(Exception):
    pass

class Book:
    def __init__(self,num,title,author):
        self.num=num
        self.title=title
        self.author=author
        self.borrowed=False

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def find_book(self,num):
        #[b1,b2]
        for i in self.books:
            if i.num == num:
                return i
            return None

    def borrow(self, num):
        book=self.find_book(num)    #book=b1
        if book is None:
            print("해당 책은 도서관에 없습니다")
            return

        if book.borrowed:
            raise AlreadyError("이 책은 이미 대출중입니다")
        book.borrowed=True


b1=Book(1,"파이썬","tom")
b2=Book(2,"클린 코드","juli")

#Library객체 생성
lib=Library()

#add_book 함수호출 2번
#self.books=[b1,b2]
#lib로 책 객체 추가 2권
lib.add_book(b1)
lib.add_book(b2)

#책 대출
lib.borrow(1)
print(b1.borrowed)

try:
    lib.borrow(1)
except AlreadyError as e:
    print("대출 실패",e)





