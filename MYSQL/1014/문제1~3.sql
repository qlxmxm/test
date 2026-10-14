-- 1. 점수가 70점 이하인 학생 이름 검색(natural join)
select stu_name, enr_grade
from student natural join enrol
where enr_grade<=70;

-- 2. 점수가 70점 이상인 학생 이름 검색(equi-join)
select stu_name, enr_grade
from student st, enrol en
where st.stu_no = en.stu_no and enr_grade>=70;

-- 3. 강종영 교수가 강의하는 과목을 수강하는 학생의 이름 검색(equi)
select stu_name, sub_prof
from student st, enrol en, subject sub
where st.stu_no=en.stu_no and en.sub_no = sub.sub_no and sub_prof='강종영';