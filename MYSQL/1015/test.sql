-- top n 질의 (limit)
-- 가장 최근에 입사한 3명 사원번호, 사원이름, 입사일 검색
select empno, ename, hiredate
from emp
order by hiredate desc
limit 3;

-- 부서별 평균급여가 가장 큰 부서 2개의 부서이름 검색(equi join)
select dname, avg(sal)
from emp, dept
where emp.deptno=dept.deptno
group by emp.deptno
order by 2 desc
limit 2;

select dname, avg(sal)
from emp, dept
where emp.deptno=dept.deptno
group by dname
order by 2 desc
limit 2;

select *from student;

select stu_no, stu_name, stu_height
from student
where stu_height is not null
order by stu_height desc
limit 5;