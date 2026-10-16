-- 변수선언
set @var1=10;
set @var2=20;

select @var1;
select @var1 + @var2;

-- if문
delimiter //
create procedure pr1()
begin
    if 5=5 then
        select '5는 5와같다';
    end if;
end //
delimiter ;

call pr1();

delimiter //
create procedure pr2()
begin
    -- 변수선언
    declare num int;
    -- 변수에 값 대입
    set num=100;
    if num=100 then
        select '100';
    else
        select '100아님';
    end if;
end //
delimiter ;
  
call pr2();

