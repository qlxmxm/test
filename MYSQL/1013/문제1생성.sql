-- 고객은 고객아이디, 이름, 비밀번호, 나이로 되어있다.
-- 고객아이디는 기본키로 지정하고 고객이름과 등급속성은 반드시 값을 입력해야하고, 
-- 적립금 속성은 값을 입력하지 않으면 0이 기본으로 입력 되도록한다.
-- 고객은 등급과 포인트로 관리되어진다.

-- 제품은 제품번호, 제품명을가지고있다.
-- 제품번호를 기본키로 지정하고 재고량이 항상 0개이상 1000개이하를 유지하도록한다.
-- 제품에서 제품의 재고량을 파악할 수있고 제품의 단가 및 제품의 제조업체에 대한 세부정보를 알수있다.

-- 고객이 제품을 주문하면 주문번호, 고객아이디, 제품번호, 수량, 주문일자를 기록한다.
-- 주문번호는 기본키로 지정하고, 고객아이디는 고객테이블의 고객아이디를 참조하는 외래키이고, 
-- 제품번호는 제품테이블의 제품번호를 참조하는 외래키가 되도록한다.






CREATE TABLE customer(
customer_id VARCHAR(50),
customer_name VARCHAR(100) NOT NULL,
password VARCHAR(100) NOT NULL,
age INT,
rating VARCHAR(20) NOT NULL,
points INT DEFAULT 0,
PRIMARY KEY(customer_id));

desc customer;

create table product(
pro_int int not null,
pro_name varchar(100),
inventory int,
price int,
manufactor varchar(100),
primary key(pro_int),
check(inventory>=0 and inventory<=1000));

desc product;

create table buy(
order_int int not null,
customer_id varchar(50) not null,
pro_int int not null,
qty int not null,
order_date date default(now()) not null,
primary key(order_int),
foreign key(customer_id) references customer(customer_id),
foreign key(pro_int) references product(pro_int));

desc buy;