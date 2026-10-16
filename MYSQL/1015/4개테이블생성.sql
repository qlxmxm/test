create table t_customer(
customer_id int not null AUTO_INCREMENT,
customer_name varchar(10) not null,
tel varchar(20) not null unique,
email varchar(50) not null unique,
address varchar(100) not null,
register_date DATETIME default now(),
region_code varchar(3) not null,
primary key(customer_id));

desc t_customer;

-- not null로 주고 기본키는 region_code로 
-- 다 varchar(3), (50)
create table t_region(
region_code varchar(3) not null primary key,
region_name varchar(50) not null);

desc t_region;

-- 테이블을 다 생성한 상태에서 참조키를 설정하고픔(제약조건 추가)
-- t_customer에 있는 region_code 가
-- t_region에 있는 region_code를 참조하게 하고 싶다.
ALTER TABLE t_customer
ADD CONSTRAINT fk_region FOREIGN KEY(region_code)
REFERENCES t_region(region_code);

-- 제약조건 확인하기
select *from
information_schema.table_constraints;

-- item_code  -> int, notnull, 자동증가 -> 기본키
-- item_name   -> 문자열, 길이 50, notnull
-- price -> int

create table t_item(
item_code int not null AUTO_INCREMENT,
item_name varchar(50) not null,
price int,
primary key(item_code));

desc t_item;

drop table t_buy;

create table t_buy(
id int not null AUTO_INCREMENT,
customer_id int not null,
item_code int not null,
qty int not null,
buy_date datetime DEFAULT now(),
primary key(id));

desc t_buy;

-- t_buy에서 cutomer_id가 t_cutomer에 있는 cutomer_id를
-- 참조하고픔
alter table t_buy
add constraint fk_customer_id4
foreign key(customer_id) references t_customer(customer_id),
add constraint fk_item_code4
foreign key(item_code) references t_item(item_code);

select *from
information_schema.table_constraints;

-- 제약조건 삭제(t_buy에서 준 fk_item_code4 제약조건 삭제)
alter table t_buy
drop foreign key fk_item_code4;

select *from
information_schema.table_constraints;