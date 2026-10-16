create table tmp_tbl(
    userid varchar(10),
    workdate DATETIME,
    bigo char(1)
);



desc tmp_tbl;

--student를 update한 후에 tmp_tb1에 값 삽입하는 트리거
-- delimiter //
-- create trigger tri1
-- -- update한 후에
-- after update
-- -- student테이블을
-- on student
-- -- update로 영향받는 각 행에 트리거 실행됨
-- for each row
-- begin
--     insert into tmp_tbl values('aa', curdate(), 'u');
-- end //
-- delimiter ;

-- delimiter 안에 -- 주석이 있으면 정상적으로 실행이 안될 수 있음
delimiter //
create trigger tri1
after update
on student
for each row
begin
    insert into tmp_tbl values('aa', curdate(), 'u');
end //
delimiter ;

-- student 에서 몸무게 -10
update student
set stu_weight=stu_weight-10;

select * from tmp_tbl;





