create table t_tbl(
t_empno int,
t_ename varchar(40),
t_job varchar(9),
t_mgr int,
t_hiredate date,
t_sal decimal(7,2),
t_comm decimal(7,2),
t_deptno int,
primary key(t_empno));

desc t_tbl;

-- int(4바이트) - (32비트)
-- tinyint (1바이트) - 8비트 -128 ~127
-- smallint (2바이트)
-- bigint(8바이트)

-- emp테이블에서 부서번호 20인 데이터만 뽑아 t_tbl에 삽입
INSERT INTO t_tbl
SELECT *
FROM emp
WHERE deptno=20;

select *from t_tbl;

-- alter : 테이블 구조 변경
-- t_tbl에 성별 컬럼 삽입 : add
alter table t_tbl add t_gender char(1);

desc t_tbl;

-- 성별 컬럼 char(1) -> varchar(1)으로 변경 : modify
alter table t_tbl modify t_gender varchar(10);

desc t_tbl;

-- 컬럼 삭제 : drop
alter table t_tbl drop t_gender;

desc t_tbl;