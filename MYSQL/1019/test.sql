-- 사용자 추가
create user 'sjw'@'localhost' identified by '1234';

-- 권한 부여
-- sjw 라는 계정으로 jw db에 접속해서 모든권한 ex)select, insert, update.. 해야할 때 권한 줌
grant all privileges on jw.* to 'sjw'@'localhost';

-- 조회권한만 줌
grant select (ename) on jw.emp to 'sjw'@'localhost';
grant select on jw.dept to 'sjw'@'localhost';

-- 권한 적용
flush privileges;

-- 권한 적용되었는지 확인
show grants for 'sjw'@'localhost';

 -- 사용자 삭제
 drop user 'sjw'@'localhost';

desc course;

 select * from course;

 select * from student;

 drop table student;

 use jw1;