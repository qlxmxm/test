-- 1. FORD 사원과 같은 급여를 받는 사원의 사원번호를검색하라. (부질의)
select empno
from emp
where sal= (select sal
from emp
where ename='FORD');

-- 2. SCOTT 사원보다 많은 급여를 받는 사원 정보를검색하라. (부질의)
select *
from emp
where sal > (select sal
from emp
where ename='SCOTT');

-- 3. ALLEN 사원보다 적은 급여를 받는 사원 정보를검색하라. (부질의)
select *
from emp
where sal < (select sal
from emp
where ename='ALLEN');

-- 4. 전체 사원의 평균 급여보다 급여가 많은 사원 정보를 검색하라. (부질의)
select *
from emp
where sal > (select avg(sal)
from emp);

-- 5. CHICAGO 지역에 위치하는 부서에 근무하는사원 정보를 검색하라. (부질의)
select *
from emp
where deptno = (select deptno
from dept
where loc='CHICAGO');