-- 부서테이블(dept)의 데이터 삭제 시 dept_del 테이블에 
-- 삭제된 데이터를 저장하는 트리거를 작성

create table dept_del(
    userid varchar(10),
    workdate datetime,
    deptno int(2),
    dname varchar(14),
    loc varchar(13)
);


DELIMITER //

CREATE TRIGGER tri_dept_del
AFTER DELETE
ON dept
FOR EACH ROW
BEGIN
    -- USER() 함수는 현재 로그인한 DB 사용자 계정을 자동으로 채워줍니다.
    -- OLD.deptno, OLD.dname, OLD.loc를 통해 방금 삭제된 부서 정보를 가져옵니다.
    INSERT INTO dept_del VALUES (USER(), NOW(), OLD.deptno, OLD.dname, OLD.loc);
END //

DELIMITER ;

select * from dept;
select * from dept_del;

-- ① 테스트용 임시 부서 하나 추가하기
INSERT INTO dept VALUES (99, 'TEST_DEPT', 'SEOUL');

-- ② 방금 넣은 99번 부서 삭제하기 (이때 트리거가 자동으로 발동합니다!)
DELETE FROM dept WHERE deptno = '99';

-- ③ 백업 테이블(dept_del)에 데이터가 잘 들어왔는지 확인하기
SELECT * FROM dept_del;




