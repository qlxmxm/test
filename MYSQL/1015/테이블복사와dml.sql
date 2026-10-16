-- 1학년 또는 2학년 조건들만 복사해서 student1 테이블 생성
create table student1
as
select *
from student
where stu_grade in(1,2);

select * from student1;

-- 과목, 수강테이블 복사해서 subject1, enrol1 생성
create table subject1
as 
select * from subject;

create table enrol1
as 
select * from enrol;

select *from subject1;
select * from enrol1;

-- 테이블의 속성과 순서대로 값 넣을거면 속성명 생략가능
insert into student1
values ('20151059','조병준', '컴퓨터정보', 1, 'B', 'M', 164, 70);

select *from student1;

-- 테이블의 속성과 순서, 개수 다를경우 속성명 적어야함
insert into student1
(stu_no, stu_name, stu_dept, stu_gender, stu_class)
values('20102038','남지선','전기전자','F','C');

select *from student1;

-- student1에 학생 테이블의 3학년 학생들의 정보 삽입하기
insert into student1
select *
from student
where stu_grade=3;

select *from student1;

select *from a_enrol;

-- 108번 과목번호만 점수 +10
update a_enrol
set enr_grade = enr_grade+10
where sub_no=107;

select *from a_enrol;

-- 수정/삭제 작업모드에서 안전모드 해제
set sql_safe_updates=0;

-- 컴퓨터개론 과목번호와 같은 과목만 +10
update a_enrol
set enr_grade = enr_grade+10
where sub_no = (select sub_no
                   from subject
                   where sub_name='컴퓨터개론');
                   
select *from a_enrol;

-- 테이블 삭제
drop table a_enrol;


CREATE TABLE a_enrol
as
SELECT *
FROM enrol
WHERE stu_no<20150000;

select *from a_enrol;

-- 데이터 삭제
delete 
from a_enrol
where stu_no=20131001;

select *from a_enrol;

-- 테이블은 남아있지만 데이터가 없다(모든 튜플을 삭제했기 때문)
delete from a_enrol;

select * from a_enrol;