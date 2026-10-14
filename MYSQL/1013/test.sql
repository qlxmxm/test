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