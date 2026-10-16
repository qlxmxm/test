-- 4. 상품 정보(product)테이블에 가장 최근에 들어온 거래처 코드 정보를 검색해라(top-n질의) - limit 1
-- 상품 코드가 문자형 숫자일 때, 가장 최근(큰 값) 순으로 정렬하여 1개만 조회
SELECT * 
FROM product1 
ORDER BY CAST(p_code AS UNSIGNED) DESC
LIMIT 1;

-- 5. 상품을 삽입하는 프로시저를 생성해라.
-- call p_pro(‘403’, ’7.1채널 스피커’, 180000, ‘스피커’)
-- 완료되었다.
DELIMITER //

CREATE PROCEDURE p_product1(
    IN v_p_code VARCHAR(3),     -- 상품 코드 입력 변수
    IN v_p_name VARCHAR(30),   -- 상품명 입력 변수
    IN v_p_cost INT,               -- 가격 입력 변수
    IN v_p_group VARCHAR(30)     -- 카테고리 입력 변수
)
BEGIN
    -- 1. 입력받은 변수 값들을 테이블에 삽입합니다.
    INSERT INTO product1 VALUES (v_p_code, v_p_name, v_p_cost, v_p_group);
    
    -- 2. 삽입이 끝나면 완료 메시지를 화면에 출력합니다.
    SELECT '완료되었다.' AS 결과;
END //

DELIMITER ;

CALL p_product1('403', '7.1채널 스피커', 180000, '스피커');

select * from product1;




