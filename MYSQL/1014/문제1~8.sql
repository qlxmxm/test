-- 1) ADAMS 사원이 근무중인 부서이름 검색해라.(equi join) 
select dname
from dept, emp
where dept.deptno = emp.deptno and ename='ADAMS';

-- 2) 급여가 2000이상인 사원들의 사원명과 지역을 검색(natural join) 
select ename, loc
from emp natural join dept
where sal > 2000;

-- 3) 2번을 equi join으로 바꾸기 
select ename, loc
from emp ,dept
where emp.deptno = dept.deptno and sal > 2000;
-- 4) 급여가 1000이상 2000이하인 사원들의 사원번호, 사원이름, 부서이름을 사원번호 순으로 검색(join using)
select empno, ename, dname
from emp join dept using(deptno)
where sal between 1000 and 2000
order by empno;
-- 5) 사원직무가 salesman이면서 chicago 지역에 근무 중인 사원명을 검색
select ename
from emp natural join dept
where job='SALESMAN' and loc='CHICAGO';
-- 6) new york이나 dallas지역에 근무하는 사원들의 사원번호, 사원이름을 사원번호 순으로 검색(equi join)
select empno, ename
from emp, dept
where emp.deptno = dept.deptno and dept.loc in("NEWYORK",'DALLAS')
order by empno;
-- 7) 부서이름이 accounting이거나 지역이 chicago 인 사원의 사원번호와 사원이름을 검색(equi join)
select empno, ename
from emp, dept
where emp.deptno=dept.deptno and dname='ACCOUNTING' or loc='CHICAGO';
-- 8) new york이나 dallas지역에 근무하는 사원들의 사원번호, 사원이름을 사원번호 순으로 검색(natural join)
select empno, ename
from emp natural join dept
where loc in ('NEWYORK','DALLAS')
order by empno;