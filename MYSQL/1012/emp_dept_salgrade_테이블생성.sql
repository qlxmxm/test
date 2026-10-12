CREATE TABLE dept(
deptno int(2),
dname varchar(14),
loc varchar(13),
constraint pk_dept PRIMARY KEY(deptno));

desc dept;

CREATE TABLE emp(
empno int(4),
ename varchar(30),
job varchar(20),
mgr int(4), -- mgr을 외래키로 설정함/ emp테이블의 empno을 참조하고 있는 외래키
foreign key(mgr) references emp(empno),
hiredate date,
sal decimal(7,2),
comm decimal(7,2),
deptno int(2),
constraint pk_emp primary key(empno));

desc emp;

CREATE TABLE salgrade(
grade decimal(7,2),
losal decimal(7,2),
hisal decimal(7,2));

desc salgrade;




insert into emp values(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,10);

insert into emp values(7566,'JONES','MANAGER',7839,'1981-4-2',2975,NULL,20);

insert into emp values(7698,'BLAKE','MANAGER',7839,'1981-5-1',2850,NULL,30);

insert into emp values(7782,'CLARK','MANAGER',7839,'1981-6-9',2450,NULL,10);

insert into emp values(7788,'SCOTT','ANALYST',7566,'1987-7-13',3000,NULL,20);

insert into emp values(7902,'FORD','ANALYST',7566,'1981-12-3',3000,NULL,20);

insert into emp values(7499,'ALLEN','SALESMAN',7698,'1981-2-20',1600,300,30);

insert into emp values(7521,'WARD','SALESMAN',7698,'1981-2-22',1250,500,30);

insert into emp values(7654,'MARTIN','SALESMAN',7698,'1981-9-28',1250,1400,30);

insert into emp values(7844,'TURNER','SALESMAN',7698,'1981-9-8',1500,0,30);

insert into emp values(7900,'JAMES','CLERK',7698,'1981-12-3',950,NULL,30);

insert into emp values(7934,'MILLER','CLERK',7782,'1982-1-23',1300,NULL,10);

insert into emp values(7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20);

insert into emp values(7876,'ADAMS','CLERK',7788,'1987-07-13',1100,NULL,20);





insert into dept values(10,'ACCOUNTING','NEW YORK');

insert into dept values(20,'RESEARCH','DALLAS');

insert into dept values(30,'SALES','CHICAGO');

insert into dept values(40,'OPERATIONS','BOSTON');



insert into salgrade values(1,700,1200);

insert into salgrade values(2,1201,1400);

insert into salgrade values(3,1401,2000);

insert into salgrade values(4,2001,3000);

insert into salgrade values(5,3001,9999);


select * from dept;
select * from emp;
select * from salgrade;

