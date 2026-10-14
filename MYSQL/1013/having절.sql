-- having(group by 조건절)
-- 학년 별 평균키 출력 // 평균키가 170이상인 데이터만 추출
select stu_grade, avg(stu_height) 
from student
group by stu_grade
having avg(stu_height) >= 170;

-- 학과별 최대 키를 추출하는데, 최대 키가 175이상만 추출
select stu_dept, max(stu_height)
from student
group by stu_dept
having max(stu_height) >= 175;