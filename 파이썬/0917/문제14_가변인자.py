#살 물건개수(수량(qty))이 재고보다 많으면 
class OutOfStockError(Exception):
    pass

#수량(qty)이 0이하면
class InvalidError(Exception):
    pass

class Product:
    def __init__(self,name,stock):
        self.name=name
        self.stock=stock

    def sell(self,qty):
        if qty<=0:
            raise InvalidError("수량은 0보다 커야 한다")
        if qty>self.stock:
            raise OutOfStockError("재고가 부족해서 팔지 못한다")

        self.stock-=qty
        
product=Product("노트북",5)  #수량 5개짜리 상품 객체 생성

#정상적인 판매
product.sell(2) #노트북 2개 팔음
print(product.stock) #3

#재고보다 많이 팔려고 시도함 ->OutOfStockError 
try:
    product.sell(10)
except OutOfStockError as e:
    print("판매실패", e)

try:
    product.sell(-1)
except InvalidError as e:
    print("판매실패", e)