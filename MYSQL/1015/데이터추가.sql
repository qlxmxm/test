insert into t_region
values
('02','서울특별시'),
('031','경기도'),
('032','인천광역시'),
('033','강원특별자치도'),
('041','충청남도'),
('042','대전광역시');

insert into t_customer (customer_name, tel, email, address, region_code)
values
('김승민','010-1234-4567','min@naver.com','서울시 종로구','02'),
('김도현','010-2345-4337','do@naver.com','경기도 수원시','031'),
('박기웅','010-2364-4557','park@naver.com','인천시 남구','032'),
('신동억','010-8854-1267','dong@naver.com','강원도 춘천시','033'),
('이다훈','010-4434-4327','lee@naver.com','대전시 중구','042');

insert into t_item(item_name,price)
values
('노트북',1500000),
('스마트폰',1000000),
('마우스',50000),
('키보드',30000),
('이어폰',100000);

select *from t_item;
select *from t_customer;
select *from t_buy;

insert into t_buy(customer_id, item_code, qty)
values
(1,1,2),
(2,2,1),
(3,3,5),
(4,4,4),
(5,5,2),
(1,2,2),
(2,4,1),
(3,5,2);