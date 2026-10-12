-- 각 테이블에 있는 전체 데이터 조회
SELECT * FROM student;
SELECT * FROM subject;
SELECT * FROM enrol;

-- 학번, 학생이름만 추출
SELECT stu_no, stu_name FROM student;

-- 학과 추출(학생테이블에서)
SELECT stu_dept FROM student;

-- 중복 제거(distinct)
select distinct stu_dept from student;

-- 원하는 별명(alias)로 데이터 가져오기
-- 학번, 과목번호, 점수 조회
select stu_no as ID, sub_no as SD, enr_grade as 성적 from enrol;

-- 점수를 +10해서 추출
select enr_grade+10 from enrol;

-- 두 개 이상의 열을 합쳐서 검색
select concat(stu_dept, stu_name) as 학과성명 from student;
select concat(stu_dept, ' ', stu_name , '입니다') as 학과성명 from student;