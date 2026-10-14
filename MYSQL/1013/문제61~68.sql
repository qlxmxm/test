-- 61. 학생의 학번, 이름, 신장을 검색하라. (신장은 첫번째 자리에서 반올림함)
select stu_no, stu_name, round(stu_height,1)
from student;

-- 62. 학생의 학번, 이름, 신장을 검색하라. (신장은 두번째 자리에서 절삭함)
select stu_no, stu_name, cast(stu_height as decimal(5,2))
from student;

-- 63. 체중을 30으로 나눈 나머지를 검색하라.
select mod(stu_weight,30)
from student;

-- 64. 신장열의 값이 널인 학생의 경우 '미기록'으로 검색하라.
select ifnull(stu_height, '미기록')
from student;

-- 65. 학생들의 성별을 소문자로 검색
select lower(stu_gender)
from student;

-- 66. 학생들의 학과, 이름을 연결하여 검색
select concat(stu_dept, stu_name)
from student;

-- 67. 학생들의 이름과 이름의 첫 2글자를 검색
select stu_name, left(stu_name,2)
from student;

-- 68. 학생들의 이름, 학과 , 그리고 학과의 두번째부터 1자리 검색
select stu_name, stu_dept, substr(stu_dept,2,1)
from student;