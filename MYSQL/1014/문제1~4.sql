-- 김인중 학생의 평균 점수보다 낮은 점수를 가진 학생의 학번과 이름을 검색해라. (서브쿼리)
select stu_no, stu_name
from student natural join enrol
where enr_grade < ( select avg(enr_grade)
from enrol natural join student
where stu_name='김인중');
-- 전체 학생의 평균 점수보다 높은 점수를 가진 학생의 학번과 이름, 과목이름, 점수을 검색해라. (서브쿼리)
select stu_no, stu_name, sub_name, enr_grade
from student natural join enrol natural join subject
where enr_grade > (select avg(enr_grade)
from enrol);
-- 점수가 학과별 학생들의 평균 점수보다 높은 학생의 학번을 검색해라. (all, (any,some)) 
select stu_no
from student natural join enrol
where enr_grade > all (select avg(enr_grade)
from enrol natural join student
group by stu_dept);
-- 기계과의 최고 점수 학생보다 최고 점수가 높은 학과의 학과명과 점수 검색해라.
select stu_dept, enr_grade
from student natural join enrol
where enr_grade > (select max(enr_grade)
from enrol natural join student
where stu_dept='기계');