-- 김인중이 수강하는 과목명과 교수이름 찾기(natural join)
-- student/ enrol/ subject
SELECT 
sub_name as 과목명, 
sub_prof as 교수이름
FROM student natural join enrol natural join subject
WHERE stu_name='김인중';

-- 강종영 교수가 강의하는 과목을 수강하는 학생의 이름 검색(join using)
SELECT stu_name as 학생이름
FROM student JOIN enrol USING(stu_no) JOIN subject USING(sub_no)
WHERE sub_prof='강종영';

-- 여학생이면서 구봉규교수의 과목을 수강하는 학생의 이름검색(natural join)
SELECT stu_name as 학생이름
FROM student NATURAL JOIN enrol NATURAL JOIN subject
WHERE stu_gender='F' and sub_prof='구봉규';

-- 시스템분석설계 과목을 수강한 학생들의 학번, 이름, 점수를
-- 점수 순으로 검색(높은순 - 내림차순) - natural join
SELECT 
stu_no as 학번,
stu_name as 이름,
enr_grade as 점수
FROM student NATURAL JOIN enrol NATURAL JOIN subject
WHERE sub_name='시스템분석설계'
ORDER BY enr_grade DESC;