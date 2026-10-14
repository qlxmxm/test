-- 부속질의(서브쿼리)
-- 옥성우 학생의 키 추출
select stu_height
from student
where stu_name='옥성우';

-- 옥성우보다 키 큰 학생의 이름 추출
select stu_name, stu_height
from student
where stu_height > (select stu_height
					from student
					where stu_name='옥성우');
                    
-- 박희철 몸무게와 같은 학생의 이름, 몸무게 추출
select stu_name, stu_weight
from student
where stu_weight=(select stu_weight
					from student
                    where stu_name='박희철') and stu_name <> '박희철';

-- 평균 키보다 큰 학생의 정보 다 출력
select *
from student
where stu_height > (select avg(stu_height)
					from student);

-- 기계학과의 반(stu_class)인 학생들 정보 다 출력
-- 기계학생이 여러명이여서 stu_class 3개로 나옴 =>  = (하나의 값과 같은가?) 비교하는 연산자
-- 여러 개의 값이 나오니까 어떤 것과 비교해야될지 모른다
SELECT *
FROM student
WHERE stu_class in (SELECT stu_class
					FROM student
                    WHERE stu_dept='기계');

-- 각 학과별 평균키보다 키가 큰 학생정보 추출
SELECT *
FROM student
WHERE stu_height > any (SELECT avg(stu_height)
					FROM student
					GROUP BY stu_dept);


SELECT *
FROM student
WHERE stu_height > all (SELECT avg(stu_height)
					FROM student
					GROUP BY stu_dept);


-- 유가인과 같은 학과인 학생의 학번, 학과 검색
select stu_no, stu_dept
from student
where stu_dept=(select stu_dept from student
				where stu_name='유가인') and stu_name <> '유가인';