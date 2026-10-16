-- 6. 상품 삭제 시(product테이블에서) product_del 테이블에 삽입이 이루어지는트리거를 작성해라.

-- p_code , p_name , p_cost , p_group은 기존 product테이블에 있는 값으로 삽입해라.

-- delete from product where p_code='201';


create table product_del
(u_id varchar(10),
wdate date,
p_code int(6),
p_name varchar(30),
p_cost int,
p_group varchar(30));

delimiter //
create trigger drop_tr
after delete
on product1
for each row
begin
insert into product_del values (u_id, now(), old.p_code, old.p_name, old.p_cost, old.p_group);
end //
delimiter ;

delete from product1 where p_code='201';

select * from product_del