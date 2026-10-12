-- 6. 과목들의 과목번호와 과목이름을 검색하라.
SELECT sub_no, sub_name FROM subject;

-- 7. 학생들의 학번과 이름, 성별을 검색하라.
SELECT stu_no, stu_name, stu_gender FROM student;

-- 8. 학생들의 모든 정보를 검색하라.
SELECT * FROM student;

-- 9. 학생들의 학번과 이름, 학년, 반을 검색하라.
SELECT stu_no, stu_name, stu_grade, stu_class FROM student;

-- 10. 과목들의 과목이름과 교수이름을 검색하라.
SELECT sub_name, sub_prof FROM subject;

​-- 11. 과목번호, 학번, 점수를 검색하라.
SELECT stu_no as ID, stu_no as SD, enr_grade FROM enrol;


-- 12. 학생들의 체중과 신장을 학번, 이름과 함께 검색하라.
SELECT stu_no, stu_name, stu_height, stu_weight FROM student;

-- 13. 학생들의 학과 중복을 제거하고 검색하라.
SELECT distinct stu_dept FROM student;

-- 14. 학생들의 성별 중복을 제거하고 검색하라.
SELECT distinct stu_gender FROM student;

-- 15. 학생들의 학년 중복을 제거하고 검색하라.
SELECT distinct stu_grade FROM student;