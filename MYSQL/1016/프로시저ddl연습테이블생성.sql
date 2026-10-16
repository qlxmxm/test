create table product1(
p_code char(3) not null,
p_name varchar(30),
p_cost int,
p_group varchar(30),
constraint product_pk primary key(p_code)
);

insert into product1 values
('101','19인치 모니터',150000,'모니터')
,('102','22인치 모니터',200000,'모니터')
,('103','25인치',260000,'모니터')
,('201','유선마우스',7000,'마우스')
,('202','무선마우스',18000,'마우스')
,('301','유선키보드',8000,'키보드')
,('302','무선키보드',22000,'키보드')
,('401','2채널 스피커',10000,'스피커')
,('402','5.1채널 스피커',120000,'스피커');


create table trade(
t_seq int not null,
p_code char(3),
c_code varchar(4),
t_date date,
t_qty int,
t_cost int,
t_tax int,
constraint trade_pk primary key(t_seq)
);

insert into trade
values (61,'131','101','2016-04-01',10,150000,150000);
insert into trade
values (5,'102','102','2016-04-26',8,200000,160000);
insert into trade
values (8,'103','101','2016-05-20',2,260000,52000);
insert into trade
values (3,'201','103','2016-04-13',7,7000,4900);
insert into trade
values (2,'201','101','2016-04-12',5,7000,3500);
insert into trade
values (9,'202','104','2016-06-02',8,18000,14400);
insert into trade
values (6,'301','103','2016-05-02',12,8000,9600);
insert into trade
values (10,'302','103','2016-06-09',9,22000,19800);
insert into trade
values (4,'401','104','2016-04-20',15,10000,15000);
insert into trade
values (11,'401','105','2016-06-15',20,10000,20000);
insert into trade
values (7,'402','102','2016-05-08',5,120000,60000);



create table customer1(
c_code varchar(4) not null,
c_name varchar(30),
c_ceo varchar(12),
c_addr varchar(100),
c_phone varchar(13),
constraint custromer_pk primary key(c_code)
);
insert into customer1 values('101','늘푸른회사','김수종','경기도 안산시','010-1234-5678');
insert into customer1 values('102','사랑과바다','박나리','경기도 평택시','010-1122-3344');
insert into customer1 values('103','대한회사','이민수','서울시 구로구','010-3785-8809');
insert into customer1 values('104','하얀기판','허진수','경상북도 포항시','010-8569-3468');
insert into customer1 values('105','한마음한뜻','하민우','인천시 남동구','010-9455-6033');



create table stock(
p_code char(3) not null,
s_qty int not null,
s_lastdate date,
constraint stock_pk1 primary key(p_code,s_qty)
);
insert into stock values('101',50,'2016-04-1');
insert into stock values('102',20,'2016-04-26');
insert into stock values('103',5,'2016-05-20');
insert into stock values('201',2,'2016-04-13');
insert into stock values('202',15,'2016-06-02');
insert into stock values('301',0,'2016-05-02');
insert into stock values('302',20,'2016-06-09');
insert into stock values('401',10,'2016-06-15');
insert into stock values('402',7,'2016-05-08');

select * from stock;