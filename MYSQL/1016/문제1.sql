-- 신입사원을 채용하였다.
-- 사원번호, 사원이름, 사원직무, 상급자사원번호, 급여, 부서번호를 입력받아
-- 사원 테이블에 삽입하는 프로시저를 작성해라.

delimiter //
create procedure new1(in a int,
in b varchar(30),
in c varchar(50),
in d int,
in e int,
in f int)

begin
insert into emp (empno,ename,job,mgr,sal,deptno)
values(a,b,c,d,e,f);

select * from emp;

end//
delimiter ;

call new1 (1,'하이', '개발',7698,3,4);




