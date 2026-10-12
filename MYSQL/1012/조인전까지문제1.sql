-- 1.사원 테이블의 구조를 검색하라.
desc emp;
-- 2.부서 테이블의 구조를 검색하라.
desc dept;
-- 3.급여 테이블의 구조를 검색하라.
desc salgrade;
-- 4.사원들의 사원번호, 사원이름, 사원직무를 검색하라.
select empno, ename, job from emp;
-- 5.부서의 부서번호와 부서이름을 검색하라.
select deptno, dname from dept;
-- 6.부서의 부서이름과 지역을 검색하라.
select dname, loc from dept;
-- 7.사원들의 급여와 커미션을 검색하라.
select sal, comm from emp;
-- 8.사원들의 입사일 중복을 제거하고 검색하라.
select distinct hiredate from emp;
-- 9.사원들의 상급자사원번호(mgr)중복을 제거하고 검색하라.
select distinct mgr from emp;
-- 10.사원들의 부서번호 중복을 제거하고 검색하라.
select distinct deptno from emp;
-- 11.사원들의 이름과 6개월 급여의 합을 검색하라.
select ename, sal*6 from emp;
-- 12.사원들의 6개월 커미션(comm)의 합을 검색하라. => sum(comm)
select sum(comm*6) from emp;
-- 13.사원이름을 ‘name’으로 사원의 급여를 ‘salary’로 열의 이름을 부여하여 검색하라.
select ename as name, sal as salary from emp;
-- 14.사원의 사원번호, 사원이름, 입사일, 부서번호를 한글로 바꾸어 검색하라.
select empno as 사원번호, ename as 사원이름, hiredate as 입사일, deptno as 부서번호 from emp;
-- 15.부서번호, 부서이름, 지역을 한글 제목으로 검색하라.
select deptno as 부서번호, dname as 부서이름, loc as 지역 from dept;
-- 16.사원의 사원직무와 사원이름을 합쳐서 검색하라.
select concat(job, ename) from emp;
-- 17.입사일(hiredate) 사원이름을 ’80-12-17에 입사한 SMITH입니다’ 식으로 검색하라.
select replace('사원이름에 입사한 SMITH입니다', '사원이름', substr(hiredate,3)) from emp;
-- 18.10번 부서에 근무하는 사원이름을 검색하라.
select ename from emp where deptno = '10';
-- 19.급여가 2000 이상인 사원들의 사원번호, 사원이름을 검색하라.
select empno, ename from emp where sal >= 2000;
-- 20.사원직무가 “CLERK”인 사원들의 사원번호, 사원이름을 검색하라.
select empno, ename from emp where job ='CLERK';
-- 21.1980년 12월 17일에 입사한 사원이름을 검색하라.
select ename from emp where hiredate = '1980-12-17';
-- 22.부서번호 30이외의 부서이름과 지역을 검색하라.
select dname, loc from dept where not deptno = '30';
-- 23.급여등급이 5인 급여의 상위급여와 하위급여를 검색하라.
select hisal, losal from salgrade where grade = '5';
-- 24.‘WARD’사원의 모든 정보를 검색하라.
select * from emp where ename = 'WARD';
-- 25.10번 부서의 근무하는 MANAGER의 사원이름을 검색하라.
select * from emp where deptno = '10' and job = 'MANAGER';
-- 26.급여가 2000이상이며, 30번 부서에 근무하는 사원들의 사원번호와 사원이름을 검색하라.
select empno, ename from emp where sal >= 2000 and deptno = '30';
-- 27.사원직무가 “CLERK”이며, 81년 이후에 입사한 사원들의 사원번호와 사원이름을 검색하라.
select empno, ename from emp where job = 'CLERK' and hiredate >= '1981-01-01';
-- 28.20부터 외에 근무하는 MANAGER의 사원이름을 검색하라.
select * from emp where not deptno = '20' and job = 'MANAGER';
-- 29.BOSTON이외 지역에 있는 부서이름을 검색하라.
select dname from dept where not loc = 'BOSTON';
-- 30.SALEMAN이며 급여가 1500이상인 사원이름을 검색하라.
select ename from emp where job = 'SALEMAN' and sal >= 1500;
select ename from emp where job = 'SALESMAN' and sal >= 1500;
-- 31.급여가 1000이상이며, 2500이하인 사원의 사원번호, 사원이름, 급여를 검색하라.
select empno, ename, sal from emp where sal between 1000 and 2500;
-- 32.사원번호가 75XX인 사원의 사원번호, 사원이름, 부서번호를 검색하라.
select empno, ename, deptno from emp where empno like '75%';
-- 33.부서번호가 10 또는 30에 근무하는 사원들의 사원이름과 급여를 검색하라.
select ename, sal from emp where deptno = '10' or deptno = '30';
-- 34.상급자사원번호가 76으로 시작하는 사원들의 사원이름을 검색하라.
select ename from emp where mgr like '76%';
-- 35.사원번호가 79로 시작하는 사원들의 사원이름, 급여, 커미션을 검색하라.
select empno, sal, comm from emp where empno like '79%';
-- 36.1981년 2월에 입사한 사원의 사원번호, 사원이름, 부서번호를 검색하라.
select empno, ename, deptno from emp where hiredate like '1981-02%';
-- 37.사원이름 중간에 ‘A’가 들어있는 사원의 사원번호와 사원이름을 검색하라.
select empno, ename from emp where ename like '_%A%_';
-- 38.상급자사원번호가 NULL인 사원의 사원번호와 사원이름을 검색하라.
select empno, ename from emp where mgr is null;
-- 39.상급자사원번호가 NULL이 아닌 사원의 사원번호, 이름, 상급자사원번호를 검색하라.
select empno, ename, mgr from emp where mgr is not null;
-- 40.사원번호가 7902 또는 7781인 사원이름을 검색하라.
select ename from emp where empno = '7902' or empno = '7781';