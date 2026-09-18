class Order:
    ORDER_STATUS=["결제대기","결제완료","배송준비","배송중","배송완료"]

    def __init__(self, order_id, customer):
        self.order_id=order_id
        self.customer=customer
        self.status="결제대기"

    def update_status(self, new_status):
        #new_status값이 리스트안에 없으면 "잘못된 상태"라고 출력
        if new_status not in self.ORDER_STATUS:
            print("잘못된 상태")
            return
        self.status=new_status
        print(f"{self.order_id} 상태가 {new_status} 로 변경되었다")

    def show(self):
        print(f"주문번호 : {self.order_id}, 주문자 : {self.customer}, 상태 : {self.status}")


#주문정보 입력
order_id1=input("첫번째 주문번호 : ")
customer1=input("첫번째 주문자: ")
order_id2=input("두번째 주문번호 : ")
customer2=input("두번째 주문자: ")

order1=Order(order_id1, customer1)
order2=Order(order_id2, customer2)

#상태변경
order1.update_status("결제완료")
order1.update_status("배송준비")
order2.update_status("배송중")
order2.update_status("문앞배송")

order1.show() #주문번호, 주문자, 상태 출력 -> f스트링으로
order2.show()