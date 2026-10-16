-- 스토어드 함수
delimiter //
create function addin(n1 int, n2 int)
    returns int

begin
    return n1+n2;

end //
delimiter ;


select addin(4,5) as '두수 합';

delimiter //
create function score1(v_enr_grade int)
	RETURNS CHAR
    
BEGIN
	DECLARE enr_score CHAR;  
    if v_enr_grade >= 90 then set enr_score:='A';
    elseif v_enr_grade >= 80 then set enr_score:='B';
		elseif v_enr_grade >= 70 then set enr_score:='C';
		elseif v_enr_grade >= 60 then set enr_score:='D';
    else set enr_score='F';
    
    end if;
	return enr_score;
    
end //
delimiter ;

select score1(90) as 'React', score1(100) as 'korean';


--  =비교연산자  
-- select
-- from
-- where stu_name='김인중';

-- := 대입연산자(변수에 값 할당)
SET @x=30;
SET @y:=50;

SELECT @x;
SELECT @y;

-- select 절에 값 할당할때는 대입연산자
select @z := count(*) from student;

delimiter //
CREATE FUNCTION prof_name(v_sub_no int)
RETURNS VARCHAR(100)
-- DETERMINISTIC
BEGIN
	DECLARE v_prof VARCHAR(100);  -- 교수명 반환받을 변수
	
    SELECT sub_prof INTO v_prof
    FROM subject
    WHERE sub_no = v_sub_no;
    
    IF v_prof is null THEN
		RETURN NULL;
    END IF;
    
    RETURN v_prof;
END //
delimiter ;


select prof_name(999);
select prof_name(111);



