-- 36. 성별이 여학생이며, 체중이 60이하인 학생을 모두 검색하라.
SELECT * FROM student WHERE stu_gender = 'F' and stu_weight <= 60;

-- 37.'컴퓨터정보'외에 1학년 학생들의 이름을 검색하라.
SELECT stu_name FROM student WHERE stu_grade = '1' and not stu_dept='컴퓨터정보';

-- 38. 학과 중 '기계'이외의 학과를 검색하라. (중복제거해서)
SELECT DISTINCT stu_dept FROM student WHERE not stu_dept='기계';;

-- 39. 컴퓨터정보과 2학년 A반 학생의 이름을 검색하라.
SELECT stu_name FROM student WHERE stu_dept='컴퓨터정보' and stu_grade = '2' and stu_class = 'A';

-- 40. 신장이 160이상이며 170이하인 학생의 학번과 이름을 검색하라
SELECT stu_no, stu_name FROM student WHERE stu_height between 160 and 170;