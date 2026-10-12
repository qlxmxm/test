-- 키가 비어있는 학생을 맨 앞에 두고, 그 다음은 학번을 큰 순서로 정렬
-- is null (참이면 1, 거짓이면 0) 를 내림차순으로 정렬하니 참(1)인행 -> 키가 null인 학생이 먼저 나옴
select *
from student
order by stu_height is null desc, stu_no desc;

-- 사칙연산
select 1+2;
select 3*(2+4)/2, 'hi';
select 10%3;

-- 문자열에 사칙연산 가하면 0으로 인식
select 'AB'+3;
select 'AB'*3;

select true, false;
select true is true;
select 2+4=6 or 2*4=7;
select 'B'='b'; -- mysql에서 기본 연산자는 대소문자 구분하지 않는다.

-- true: 1 / false: 0
select 10 between 15 and 20;
select 'apple' not between 'banana' and 'computer';

select 1+2 in (2,3,4);
select 'hi' in (1, true, 'hi');

-- 문자열 단일 행 함수
select concat('hello',' ','2026','10','12') as 날짜;

-- null값이 하나라도 있으면 null로 반환됨
select concat('hello',' ',null,'2026','10','12') as 날짜;

-- 첫번째 매개변수로 이어붙여짐
-- concat with separator
select concat_ws('-',2026,10,12,'Date');

-- null값 있어도 null 무시되고 출력
select concat_ws('-',2026, null, 10,12,'Date');

-- 3번째 위치에서 ~ 끝까지
select substr('ABCDEFGH',3);

-- 3번째 위치에서 ~ 2글자 개수
select substr('ABCDEFGH',3,2);

-- 끝에서부터 4번째 위치
select substr('ABCDEFGH', -4);

-- 끝에서부터 4번째 위치에서 2글자 개수
select substr('ABCDEFGH', -4,2);

-- 문자열 바이트 길이
select length('ABCDEFGH'); -- 영문자 1바이트씩
select length('안녕하십니까'); -- 한글은 3바이트씩

-- 문자열의 문자 길이
select char_length('안녕하십니까');
select char_length('ABCDEFGH');


-- lpad(s,n,p) : s가 n이 될때까지 p를 왼쪽에 이어붙임
select lpad('AB',5,'#');  -- left pad

-- rpad(s,n,p) : s가 n이 될때까지 p를 오른쪽에 이어붙임
select rpad('AB',5,'@');  -- right pad

select replace('버거킹에서 버거킹 햄버거를 먹었다', '버거킹', 'KFC');

-- instr(S,s) : S 중 s의 첫 위치 반환
select instr('ABCDE', 'ABC');
select instr('ABCDE', 'BC');
select instr('ABCDE', 'C');