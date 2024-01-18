# Write your MySQL query statement below
SELECT CASE WHEN COUNT(*) > 0 THEN MAX(num) ELSE NULL END AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS unique_numbers;