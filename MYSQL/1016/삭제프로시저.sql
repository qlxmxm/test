-- 이름에 'M' 이 들어간 사원들을 다 삭제하는 프로시저(del_name)

delimiter //
CREATE PROCEDURE del_name()

BEGIN
    delete from emp
    where ename like '%M%'

END //
delimiter ;

call del_name();


-- delimiter //
-- CREATE PROCEDURE del_name(in d_ename vachar(30))

-- BEGIN
--     delete from emp
--     where ename like concat('%', d_ename, '%')

-- END //
-- delimiter ;

-- call del_name('M');