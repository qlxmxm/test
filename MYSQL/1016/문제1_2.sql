-- order_id	customer_id	customer_name	product_id	product_name	category_name

-- 1	C1	홍길동	P1	노트북	전자제품
-- 1	C1	홍길동	P2	마우스	전자제품
-- 2	C2	김철수	P3	의자	가구
-- 3	C1	홍길동	P3	의자	가구



-- - customer_id, customer_name은 order_id 만 알면 결정된다고 가정 -> product_id는 필요없다(2NF 위반)

-- - pruduct_name, category_name은 product_id만 알면 결정된다고 가정-> order_id는 필요없다(2NF 위반)

-- 1. 이 테이블의 기본키는 무엇인가?
-- 1 : pk=(order_id, product_id)

-- 2. 정규형(2NF)을 위반하는 컬럼을 모두 찾으세요
-- 2 : customer_id , customer_name , product_name , category_name

-- 3. 3정규형(3NF)을 위반하는 컬럼을 찾으세요
-- 3 : customer_name, category_name

-- 3NF까지 만족하도록 테이블을 분해하세요
-- 주문(order_id, customer_id)
-- 고객(customer_id, customer_name)
-- 상품(product_id, product_name)
-- 카테고리(category_id, category_name)
-- 주문-상품(order_id, product_id) : 관계파악

