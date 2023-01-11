-- 두 테이블이 주어지고 한쪽 테이블만 가지고 있는 데이터를 조회하는 문제
-- RIGHT JOIN을 이용해 오른쪽 테이블만 가지고 있는 데이터까지 모두 조회했고
-- 추가로 WHERE 절을 사용하여 오른쪽 테이블만 가지고 있는 데이터만을 조회했다.

SELECT o.ANIMAL_ID, o.NAME
FROM ANIMAL_INS i RIGHT JOIN ANIMAL_OUTS o
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.ANIMAL_ID IS NULL