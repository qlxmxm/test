
start TRANSACTION;

UPDATE emp
set sal=sal+1000
where empno=7566;   -- sal :29000

select *from emp;

UPDATE emp
set sal=sal+2000
where empno=7788;    -- sal : 31000

select *from emp;

-- 변경사항 영구저장
commit;


UPDATE emp
set sal=sal+1000
where empno=7566;  -- sal :4975

select *from emp;

SAVEPOINT sp1;  -- 현재 상태 저장 / 첫번째 저장점 설정 


UPDATE emp
set sal=sal+2000
where empno=7788;    -- sal : 33000

select *from emp;

SAVEPOINT sp2;   -- 두번째 저장점 설정

ROLLBACK TO sp1;   -- sp1 이후의 변경만 취소되었다.

commit;