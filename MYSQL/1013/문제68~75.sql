-- 68. 학생 중 키가 가장 큰 학생의 신장을 검색하라.
select max(stu_height)
from student;
-- 69. 학생의 이름 중 MAX와 MIN값을 검색하라.
select max(stu_name), min(stu_name)
from student;
-- 70. 학생테이블의 레코드(튜플)수를 검색하라.
select count(*)
from student;
-- 71. 학과별 학생들의 인원수를 검색하라.
select stu_dept, count(*)
from student
group by stu_dept;
-- 72. 학과별 학생들의 인원수를 인원수가 많은 순으로 검색하라.
select stu_dept, count(*)
from student
group by stu_dept
order by 2 desc ,1;
-- 73. 학년별 학생들의 인원수를 검색하라.
select stu_grade, count(*)
from student
group by stu_grade;
-- 74. 학과별 학년별 학생들의 평균 체중을 검색하라.
select stu_dept, stu_grade, avg(stu_weight)
from student
group by stu_dept, stu_grade;
-- 75. 학과별 학년별 학생들의 학번의 MAX와 MIN값을 검색하라.
select stu_dept, stu_grade, max(stu_no), min(stu_no)
from student
group by stu_dept, stu_grade;