-- 16. 학생들의 학과, 학년 중복을 제거하고 검색하라.
select distinct stu_dept,stu_grade from student;

-- 17. 학생들의 학과, 반 중복을 제거하고 검색하라.
select distinct stu_dept,stu_class from student;

-- 18. 학생들의 체중을 5만큼 증가시킨 값을 검색하라.
select distinct stu_weight+5 from student;

-- 19. 학생들의 체중을 5만큼 감소시킨 값을 검색하라.
select distinct stu_weight-5 from student;

-- 20. 학생들의 학번과 이름을 별칭 "학번", "이름"으로 부여하여 검색하라.
select distinct stu_no as 학번, stu_name as 이름 from student;

-- 21. 수강(enrol)테이블의 모든 정보를 검색하라.
select * from enrol;

-- 22. 학생 테이블에서 학과명과 이름을 합쳐서 검색하라.
select concat(stu_dept, stu_name) as 학과성명 from student;

-- 23. 학생의 이름과 학과를 '컴퓨터정보과 옥한빛입니다'식으로 검색하라.
select concat(stu_dept,'과 ', stu_name,'입니다') as 학과성명 from student;

-- 24. 컴퓨터정보 학생들을 검색하라.
select distinct * from student where stu_dept='컴퓨터정보';

-- 25. 기계과 학생들을 검색하라.
select distinct * from student where stu_dept='기계';