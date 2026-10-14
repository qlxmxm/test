-- 기존에 있는 테이블을 복사해서 생성
-- 2015이전의 학번들만 뽑아서 a_enrol생성
-- CREATE TABLE a_enrol
-- as
-- SELECT *
-- FROM enrol
-- WHERE stu_no < 20150000;

select * from a_enrol;

-- ddl(data definition language) : create, drop, alter
-- dml(data manipulation language) : insert, delete, update
-- dcl(data control language) : rollback, commit

-- insert into a_enrol values(108,20153212,91);

select * from a_enrol
where stu_no > 20150000;

-- 2015로 시작하는 학번만 추출해서 b_enrol테이블 생성(like)
-- CREATE TABLE b_enrol
-- as
-- SELECT stu_no
-- FROM enrol
-- where stu_no like '2015%';

select * from b_enrol
where stu_no like '2015%';
