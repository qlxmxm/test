-- 급여가 제일 높은 사원이름을 출력하는 함수

delimiter //
create function max_sal()
returns char(100)

begin
declare v_ename char(100);

select ename into v_ename
from emp
order by sal desc
limit 1;

return v_ename;
end //
delimiter ;

select max_sal();