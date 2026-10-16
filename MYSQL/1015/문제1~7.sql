-- 1. 각 지역별로 고객의수 뽑기(left join)

select region_name, count(customer_name)
from t_region left join t_customer
on t_region.region_code = t_customer.region_code
group by t_region.region_code;

-- 2. customer_id 3이 구매한 제품의 이름 출력
select item_name
from t_item natural join t_buy
where customer_id=3;


-- 3. 제품의 평균 가격보다 높은 가격을 가진 제품의 이름과 가격 출력
select item_name, price
from t_item
where price > (select avg(price)
from t_item);


-- 4. 고객 별 구매한 총 제품의 수 출력
select customer_name, qty
from t_buy natural join t_customer;

-- 5. 고객 새로 가입했다. 추가
insert into t_customer(customer_name, tel, email, address, region_code)
values('김태현', '010-3355-3399', 'hyun@naver.com', '대전시 서구 ', '042');

select * from t_customer;

-- 6. 김도현 고객 주소 수정 -> 경기도 하남시로 바꿔라.
update t_customer
set address= '경기도 하남시'
where customer_name='김도현';

-- 7. 김태현 고객이 스마트폰 2개 주문했을 경우 구매 테이블에다 추가해라.
insert into t_buy (customer_id, item_code, qty)
value (6, 2, 2);