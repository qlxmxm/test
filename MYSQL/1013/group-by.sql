-- 그룹함수
-- 점수의 총합
select sum(enr_grade) from enrol;

select max(enr_grade) as 제일높은점수,
min(enr_grade) as 제일낮은점수 from enrol;

select count(*) from student; -- 행 개수

-- count(컬럼명)은 null값 세지 않음
-- stu_height 값이 있는 행의 개수 출력
select count(stu_height) from student; 

-- 중복제거한 stu_dept 행의 개수 
select count(distinct stu_dept) from student;

select avg(stu_height) from student;

-- select from
-- select from where 
-- select from (where) order by 
-- select from (where) group by order by 

-- group by 
-- 학과를 그룹별로 묶어 행의 개수, 학과 추출
select count(*), stu_dept
from student
group by stu_dept;

-- 학과를 그룹별로 묶어 몸무게가 50이상인 학생들 수 추출
select stu_dept, count(*)
from student
where stu_weight>=50
group by stu_dept;

-- 학과를 그룹별로 묶어 몸무게가 50이상인 학생들 수 추출
-- count(*) 개수 작은순서대로(오름차순), stu_dept로 오름차순
select stu_dept, count(*)
from student
where stu_weight>=50
group by stu_dept
order by 2,1;

-- 학과, 학년을 그룹화해서 학생의 수 추출
select stu_dept, stu_grade, count(*)
from student
group by stu_dept, stu_grade;

-- 학과별 학생의 키 평균
select stu_dept, avg(stu_height)
from student
group by stu_dept;

-- 학과별 학생의 몸무게 평균(소수점 첫째자리까지)
select stu_dept, format(avg(stu_weight),1)
from student
group by stu_dept;