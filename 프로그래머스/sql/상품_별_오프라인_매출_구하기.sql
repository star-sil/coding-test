-- SQL 실행 순서 FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
-- GROUP BY는 주로 aggregate function(COUNT, MAX, MIN, SUM, AVG)와 함께 쓰인다.
-- SELECT 절에는 GROUP BY에 쓰인 column만 사용가능하다.

SELECT p.PRODUCT_CODE, SUM(p.PRICE * o.SALES_AMOUNT) AS SALES
FROM PRODUCT p JOIN OFFLINE_SALE o
ON p.PRODUCT_ID = o.PRODUCT_ID
GROUP BY p.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE ASC