create table emp500(
    empno int(4),
    ename varchar(10),
    workdate datetime
);

desc emp500;

delimiter //
create trigger tri3
after insert
on emp
for each row
begin
    if new.sal > 5000 then
        insert into emp500 values(new.empno, new.ename, now());
    end if;

end //
delimiter ;

select * from emp;

insert into emp values(1111,'gildong','student',7839,now(),5600,null,10);
insert into emp values(2222,'jack','student',7839,now(),4600,null,10);

select * from emp500;







