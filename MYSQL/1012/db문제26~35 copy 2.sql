-- 26. 전기전자과 학생들을 검색하라.
SELECT * FROM student WHERE stu_dept = '전기전자';

-- 27. 신장이 170이상인 학생들을 검색하라.
SELECT * FROM student WHERE stu_height >= 170;

-- 28. 체중이 65이상인 학생들을 검색하라.
SELECT * FROM student WHERE stu_weight >= 65;

-- 29. 기계 학생들의 학번, 이름을 검색하라.
SELECT stu_no, stu_name FROM student WHERE stu_dept = '기계';

-- 30. 컴퓨터정보 학생들의 학번, 이름을 검색하라.
SELECT stu_no, stu_name FROM student WHERE stu_dept = '컴퓨터정보';

-- 31. 남학생의 이름을 검색하라.
SELECT stu_name FROM student WHERE stu_gender = 'M';

-- 32. 전기전자과 이외 학생들의 모든 정보를 검색하라.
SELECT * FROM student WHERE stu_dept <> '전기전자';

-- 33. 점수가 80점 이상인 학생들의 학번을 검색하라.
SELECT * FROM enrol WHERE enr_grade >= 80;

-- 34. '김인중'학생의 모든 정보를 검색하라.
SELECT * FROM student WHERE sub_name = '김인중'

-- 35. '기계'과 이고 2학년인 학생들의 모든 정보를 검색하라.
SELECT stu_no, stu_name FROM student WHERE stu_dept = '기계' AND stu_grade = 2;