-- 1. 데이터모델링
-- 2. 조인(join)
-- 2.1 내부조인(inner join)
-- (equi join, natural join, join~using, join~on)
-- 2.2 외부조인(outer join)
-- 2.3 자체조인(self join)
-- 2.4 교차조인(cross join) 

use jw;
-- 학번, 이름, 학과, 점수 추출
-- equi join
-- 1) 모든 테이블에서 일치하는 속성 찾기
-- 2) 일치하는 속성과 연결(테이블 명시)
select st.stu_no, stu_name, stu_dept, enr_grade
from student st, enrol en
where st.stu_no = en.stu_no;

-- natural join(자연조인)
-- 공통 속성을 안 적어줘도 됨
select st.stu_no, stu_name, stu_dept, enr_grade
from student st natural join enrol en;

-- (inner)join~using(공통속성)
SELECT stu_no, stu_name, stu_dept, enr_grade
from student inner join enrol using(stu_no);

-- (inner)join~on
SELECT stu.stu_no, stu_name, stu_dept, enr_grade
from student stu join enrol en on stu.stu_no=en.stu_no;