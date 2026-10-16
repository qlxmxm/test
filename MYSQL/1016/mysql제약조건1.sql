create table new_emp2(
no int primary key,
name varchar(20) not null,
jumin varchar(10) not null unique,
loc_code int check(loc_code<5),
deptno int,
foreign key(deptno) references dept(deptno));

desc new_emp2;

-- name에 unique 제약 조건 추가 (emp_uk)
alter table new_emp2 add constraint emp_uk unique(name);

-- loc_code에 not null 수정
-- alter table new_emp2 modify loc_code int not null;
alter table new_emp2 modify column loc_code int not null;

desc new_emp2;

-- no에 외래키 추가(emp.empno 참조) 
alter table new_emp2 add constraint
foreign key(no) references emp(empno);

-- 제약 조건 조회
select * from information_schema.table_constraints;

-- 부모테이블에서 속성이 unique or pk(unique+not null) 여야 참조가 가능하다.