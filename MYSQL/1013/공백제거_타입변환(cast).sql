-- 왼쪽 공백제거(left trim)
select concat('|', ltrim('         hello'), '|');
-- 오른쪽 공백제거(right trim)
select concat('|', rtrim('    hello          '), '|');
-- 양쪽 공백제거(trim)
select concat('|', trim('    hello          '), '|');

-- cast(A as T) : A를 T 자료형으로 변환
select '011'='11'; -- false
select cast('011' as decimal); -- 11
select cast('11' as decimal); 
select cast('011' as decimal) = cast('11' as decimal); -- true


-- decimal(a,b) : a 는 최대 자리수(한도), b는 소수점 자리수
select cast('123.456' as decimal(5,2)); -- 반올림
select cast('12' as decimal(5,2));
select cast('1.5' as decimal(5,2)); -- 1.50