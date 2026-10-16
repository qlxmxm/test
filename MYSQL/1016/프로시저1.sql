-- 저장 프로시저(미리 정의된 sql 집합)
-- Stored Procedure(SP)

-- 학번이 입력해서 이름 출력하는 프로시저
delimiter //

CREATE PROCEDURE test(
    in v_stu_no int,
    out v_stu_name varchar(12))

-- stu_name을 v_stu_name에 넣겠다.
-- 내가 입력한 학번이 학생테이블에 있는 학번과 일치한 학생이름을 v_stu_name에 넣음
BEGIN
    select stu_name into v_stu_name
    from student
    where stu_no=v_stu_no;

end //

delimiter ;

-- 프로시저 호출
-- 20153075에 맞는 학생명을 d_stu_name에 받는다.
call test(20153075, @d_stu_name);

select @d_stu_name;



