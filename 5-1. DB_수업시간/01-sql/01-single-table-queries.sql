-- 01. Querying data
SELECT LastName FROM employees;

SELECT 
    LastName, FirstName 
FROM 
    employees;

SELECT * FROM employees;

SELECT FirstName AS '이름' FROM employees;

SELECT 
    Name, 
    Milliseconds / 60000 AS '재생시간 (분)'
FROM 
    tracks;


-- 02. Sorting data

SELECT FirstName
FROM employees
ORDER BY FirstName ASC;

SELECT FirstName
FROM employees
ORDER BY FirstName DESC;

SELECT Country, City
FROM customers
ORDER BY Country DESC, City ASC;

SELECT 
    Name, 
    Milliseconds / 60000 AS '재생시간 (분)'
FROM 
    tracks
ORDER BY 
    Milliseconds DESC;


-- NULL 정렬 예시

SELECT ReportsTo
FROM employees
ORDER BY ReportsTo ASC;

SELECT ReportsTo
FROM employees
ORDER BY ReportsTo DESC;


-- 03. Filtering data

-- 중복제거 DISTINCT
SELECT DISTINCT
    Country
FROM 
    customers
ORDER BY
    Country ASC;

-- 특정 검색 조건 지정 WHERE
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
    -- Bytes >= 100000
    -- AND Bytes <= 500000;
    Bytes BETWEEN 100000 and 500000;


SELECT
    Name, Bytes
FROM
    tracks
WHERE
    Bytes BETWEEN 100000 and 500000
ORDER BY
    Bytes ASC;


SELECT
    LastName, FirstName, Country
FROM
    customers
WHERE
    -- Country = 'Canada'
    -- OR Country = 'Germany'
    -- OR Country = 'France';
    Country IN ('Canada', 'Germany', 'France');
    -- Country NOT IN ('Canada', 'Germany', 'France');

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


SELECT 
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY
    Bytes DESC
LIMIT
    7;

SELECT 
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY
    Bytes DESC
LIMIT
    3, 4;
-- LIMIT 4 OFFSET 3;


-- 04. Grouping data

SELECT
    Country, COUNT(*) AS '인원수'
FROM
    customers
GROUP BY
    Country;


SELECT
    Composer, 
    AVG(Bytes) AS avgOfBytes
FROM
    tracks
GROUP BY
    Composer
ORDER BY
    AVG(Bytes) DESC;


SELECT
    Composer, 
    AVG(Bytes) AS avgOfBytes
FROM
    tracks
GROUP BY
    Composer
ORDER BY
    avgOfBytes DESC;


SELECT
    Composer,
    AVG(Milliseconds / 60000) AS avgOfMinute
FROM
    tracks
GROUP BY
    Composer
-- 그룹핑한 데이터에 조건 걸 때는 HAVING 사용
HAVING
    avgOfMinute < 10;



