-- 문자 대/소문자 변환
select upper('korea'); 
select lower('KOREA');

-- round(실수, 반올림할 자리수)
select round(345.678); -- 반올림할 자리수 안적으면 소수점 첫째자리에서 반올림해서 정수로 만든다.
select round(345.678,0); -- 소수점 아래 0자리까지 남겨!!!!
select round(345.678,1); -- 소수점 아래 1자리 남겨!!!!(둘째자리에서 반올림)
select round(345.678,-1); -- 소수점 왼쪽(정수부에서 반올림)/ 일의자리에서 반올림해줘!!!!
select round(345.678,-2); -- 소수점 왼쪽(정수부에서 반올림)/ 십의자리에서 반올림해줘!!!!

-- 절대값
select abs(-1), abs(3-10);

-- 밑수와 지수/제곱근
select pow(2,3), power(5,2), sqrt(16);

select truncate(1234.5678,1); -- 소수점 첫째자리까지 출력 후 버림
select truncate(1234.5678,2);
select truncate(1234.5678,-1); -- 반올림없이 그냥 버린다. -1 => 일의 자리 버린다.
select truncate(1234.5678,-2); 
select truncate(1234.5678,-3); 

select mod(10,4); -- 나머지
select ceil(10.3); -- 올림
select floor(10.7); -- 내림

-- 날짜함수
select now(); -- 현재 년월일시분초
select sysdate();  -- 현재 년월일시분초
select timestamp(now()); -- 현재 년월일시분초

select time(now()); -- 시분초

select date(now()); -- 년월일
select curdate(); -- 년월일

select adddate(now(), interval 1 day); -- 오늘 기준으로 다음날
select adddate('2026/10/13',1);
select date_add(now(), interval 1 day); -- date_add는 interval써야함

-- 오늘 기준으로 다음 달
select date_add(now(), interval 1 month);

-- 오늘 기준으로 일주일 전
select date_sub(now(), interval 1 week);

-- 2026년 12월 31일의 다음 날 추출
select adddate('2026/12/31' ,1);

-- 월:0, 화:1, 수:2, 목:3, 금:4, 토:5, 일:6
-- weekday() : 요일을 숫자로 반환
select weekday(curdate());

-- 오늘 기준으로 1을 더한 날짜
select adddate(curdate(), weekday(curdate()));

-- 오늘 기준으로 1을 뺀 날짜
select adddate(curdate(), -weekday(curdate()));

select curtime();