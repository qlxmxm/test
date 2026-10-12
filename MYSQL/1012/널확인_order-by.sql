-- 널 값 존재 여부 
select stu_no, stu_name, stu_height
from student
where stu_height is null;

select stu_no, stu_name, stu_height
from student
where stu_height is not null;

-- 학과가 컴퓨터정보 또는 기계학과 학생들 다 추출 
-- in / or
select *
from student
where stu_dept in ('컴퓨터정보', '기계');

select *
from student
where stu_dept='컴퓨터정보' or stu_dept='기계';

-- 순서화(정렬)
select stu_no, stu_name
from student
order by stu_no; -- 오름차순(asc 생략가능)

select stu_no, stu_name
from student
order by stu_no desc; -- 내림차순(desc 생략 불가능)

-- 별칭이 붙어있는 열을 기준으로 정렬
select stu_no, stu_name, stu_dept, stu_weight-5 as target
from student
order by target, stu_name; -- target이 먼저 정렬되고 그 이후에 stu_name이 정렬

-- 열의 순서번호 이용하여 정렬
select stu_no, stu_name, stu_dept, stu_weight-5 as target
from student
order by 4; -- 열의 4번째 컬럼에 있는 속성으로 정렬

select stu_no, stu_name, stu_dept, stu_weight-5 as target
from student
order by stu_weight-5;

-- order by에 차순 안적으면 기본이 asc임
select stu_no, stu_name, stu_dept, stu_weight-5 as target
from student
order by stu_dept, target; -- 학과가 먼저 정렬되고 그 이후에 target정렬됨

-- 위의 코드를 열의 순서로 정렬
select stu_no, stu_name, stu_dept, stu_weight-5 as target
from student
order by 3,4;

select stu_no, stu_name, stu_dept, stu_weight-5 as target
from student
order by stu_dept desc, target desc;