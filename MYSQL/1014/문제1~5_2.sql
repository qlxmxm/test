-- 1. 컴퓨터정보과 학생들의 평균 점수를 구해 학생들의 학번, 이름, 평균 점수를 성적 순으로 출력
select stu_no, stu_name, avg(enr_grade)
from student natural join enrol
where stu_dept = "컴퓨터정보"
group by stu_no
order by avg(enr_grade) desc;

-- 2. 시스템분석설계 과목을 수강한 학생들의 학번, 이름, 점수를 성적 순으로 검색해라.
select stu_no, stu_name, enr_grade
from student natural join enrol natural join subject
where sub_name='시스템분석설계'
order by enr_grade desc;

-- 3. 두 과목 이상 수강한 학생들의 학번, 이름, 수강과목 수를 수강과목이 많은 순으로 검색해라.
select stu_no,stu_name,count(sub_no)
from student natural join enrol
group by stu_no
having count(sub_no)>=2
order by count(sub_no) desc;
-- 4. 한 과목을 수강한 학생들의 학번, 이름을 학과별 학번 순으로 검색해라.
select stu_no, stu_name
from student natural join enrol
group by stu_no
having count(sub_no)=1
order by stu_dept,stu_no;
-- 5. 컴퓨터개론과 시스템분석설계 과목을 수강하는 학생의 학번, 이름을 학번순으로 검색해라.
select stu_no, stu_name
from student natural join enrol natural join subject
where sub_name in ('컴퓨터개론','시스템분석설계')
group by stu_no
having count(sub_name)=2
order by stu_no