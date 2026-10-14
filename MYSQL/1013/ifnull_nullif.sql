select stu_name, if(stu_gender='F', '여자','남자')
from student;

-- p.152
select stu_name, ifnull(stu_height,0)
from student;

-- nullif(인수1, 인수2) : 두개값 비교해서 같으면 null반환
--                     같지 않으면 인수 1반환
select nullif('A','A');
select nullif('B','A');

select ifnull(nullif('A','A'),'널값');
-- select ifnull(null, '널값');

-- 학과가 컴퓨터정보학과면 null값, 그 외는 학과명 출력
-- nullif로 구현
select nullif(stu_dept, '컴퓨터정보')
from student;