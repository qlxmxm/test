-- 오른쪽 외부조인
-- 오른쪽 테이블은 모든 행을 유지하고 왼쪽에서 sub_no가 일치하는 행만 붙는다.
select sub.sub_no, sub_name
from enrol en right join subject sub 
on en.sub_no=sub.sub_no;

-- 왼쪽 테이블 기준으로 오른쪽 테이블을 합친다.
select sub.sub_no, sub_name
from enrol en left join subject sub 
on en.sub_no=sub.sub_no;

-- self join(자체조인)
select a.empno as 사원번호, 
a.ename as 사원이름,
b.empno as 상급자사원번호,
b.ename as 상급자이름
from emp a join emp b
on a.mgr=b.empno;

-- cross join(교차조인)
-- 테이블의 모든 행이 각각 한번씩 조인되어 모든 경우의 수 조합됨
select student.*, enrol.*
from student cross join enrol;