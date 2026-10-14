-- 그룹함수와 조인 활용
-- 과목을 2개 이상 듣고 있는 학생의 이름을 이름 순으로 검색
-- student, enrol
SELECT stu_name, count(sub_no)
FROM student NATURAL JOIN enrol
GROUP BY stu_no
HAVING count(sub_no) >=2
ORDER BY 1;


-- 점수가 평균보다 높은 학번, 이름, 과목명, 점수 출력
-- enrol student, subject
SELECT stu_no, stu_name, sub_name, enr_grade
FROM student NATURAL JOIN enrol NATURAL JOIN subject
WHERE enr_grade > (SELECT avg(enr_grade) 
                    FROM enrol);