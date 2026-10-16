
delimiter //
create trigger tri2
after update
on student
for each row
-- update일어나기 전에 student테이블의 stu_weight가 40보다 크면
-- tmp_tbl에 데이터 삽입
begin
    if(old.stu_weight > 40.00) then
    insert into tmp_tbl values('aabb',now(),'A');
    end if;
end //
delimiter ;

update student
set stu_weight=stu_weight+3;

select * from student;

select * from tmp_tbl;





