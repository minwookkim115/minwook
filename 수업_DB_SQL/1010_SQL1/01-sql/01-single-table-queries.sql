-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  *
FROM
  employees;

-- 필드명 바꾸기
SELECT
  FirstName AS '이름'
FROM
  employees;

-- 숫자로 나누기
SELECT
  Name, Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks;

-- 02. Sorting data
-- 오름차순
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName ASC;

-- 내림차순
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City ASC;

SELECT
  Name, Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;

-- 03. Filtering data
-- 중복제거
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

-- 조건을 지정(WHERE)
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000;
-- WHERE
--   Bytes >= 100000
--   AND Bytes <= 500000;

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');
--   Country = 'Canada'
--   OR Country = 'Germany'
--   OR Country = 'France';

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';

-- 조건 지정(LIMIT)
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;

-- 04. Grouping data
-- DISTINCT하고 ORDER BY 한거랑 똑같음
-- COUNT => 몇개 있나 세보자
SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT
  Composer, AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;

SELECT
  Composer, AVG(Milliseconds / 60000)
FROM
  tracks
GROUP BY
  Composer
HAVING -- GROUP BY 하면 HAVING 써야함
  AVG(Milliseconds / 60000) < 10;


-- 에러


-- 에러 해결
