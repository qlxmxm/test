-- where 절 사용 (where 절의 문자열, 날짜 - 작은따옴표/큰따옴표)

SELECT stu_name, stu_dept, stu_grade, stu_class 

FROM student

WHERE stu_dept='컴퓨터정보';



-- 두가지 조건 이상 다 만족해야할 때 and절로 연결

SELECT stu_name, stu_dept, stu_grade, stu_class 

FROM student

WHERE stu_dept='컴퓨터정보' and stu_grade=2;



-- 원하는 개수만큼 데이터 가져오기

select * from student limit 5;

select * from student;

-- 인덱스 1부터 5개

select * from student limit 1,5;



-- 범위조건(between A and B) (이상 ~ 이하)

SELECT *

FROM student

WHERE stu_weight between 60 and 70;



SELECT *

FROM student

WHERE stu_no between '20140001' and '20149999'; -- 사전 순(문자비교)



-- 학번, 이름, 학과 추출

SELECT stu_no, stu_name, stu_dept

FROM student

WHERE stu_dept in ('컴퓨터정보','기계');



-- % : 0개 이상 문자

-- _ : 1개 문자와 대응



-- 김씨인 학생 학번, 이름, 학과 조회

SELECT stu_no, stu_name, stu_dept

FROM student

WHERE stu_name LIKE '김%';



-- 두번째 '수'가 들어간 이름의  학번, 이름, 학과 조회

SELECT stu_no, stu_name, stu_dept

FROM student

WHERE stu_name LIKE '_수%';

-- 2014로 시작하는 학번(student테이블에서)

SELECT stu_no

FROM student

WHERE stu_no LIKE '2014%';



-- 이외

-- 컴퓨터정보학과 아닌 학생들의 속성 다 출력

-- p.134

SELECT *

FROM student

WHERE not stu_dept='컴퓨터정보';



SELECT *

FROM student

WHERE stu_dept not in ('컴퓨터정보');



SELECT *

FROM student

WHERE stu_dept <> '컴퓨터정보';



SELECT *

FROM student

WHERE stu_dept != '컴퓨터정보';