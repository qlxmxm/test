-- 56. 학생들의 이름과 이름의 길이를 검색하라.
select stu_name, char_length(stu_name) from student;

-- 57. 학생들의 학과와 학과명의 길이를 검색하라.
select stu_dept, char_length(stu_dept) from student;

-- 58. 학생들의 이름에 '김'이 처음 몇번째 있는지 검색하라.
select stu_name, instr(stu_name, '김') from student;

-- 59. 학생의 이름을 15자리로 하고, 뒤에 '&'를 채워 검색하라.
select rpad(stu_name,15,'&')from student;

-- 60. 학생의 학과를 20자리로 하고, 앞에 '%'를 채워 검색하라.
select lpad(stu_dept,20,'%') from student;