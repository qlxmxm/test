-- 학생의 점수를 +10점 올리고(학번, 과목번호 일치하면)
-- 그 결과 저장하는 프로시저

delimiter //
CREATE PROCEDURE test3(
    in v_stu_no char(8),
    in v_sub_no char(3),
    inout v_enr_grade int)

BEGIN
    update enrol
    set enr_grade = enr_grade + v_enr_grade
    where stu_no=v_stu_no and sub_no=v_sub_no;

    -- 학번, 과목변호가 같으면 위에서 증가시킨 성적을 v_enr_grade
    -- 에 저장하려고

    select enr_grade into v_enr_grade
    from enrol
    where stu_no=v_stu_no and sub_no=v_sub_no;

end //
delimiter ;

-- 변수 선언(set @변수명)
set @d_ner_grade=10;
call test3(20153075,105,@d_ner_grade);

select * from enrol;

drop PROCEDURE test3;

