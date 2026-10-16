-- 1. 20153088학생이 자퇴하였다.
delete
from student1
where stu_no='20153088';

-- 2. 과목번호 112, 과목이름 자동화시스템, 교수명 고종민, 학년 3, 학과 기계가 추가되었다.
insert into subject1
values(112,'자동화시스템','고종민',3,'기계');

-- 3. 과목번호 110이 501로 변경되었다.
update subject1
set sub_no = 501
where sub_no=110;