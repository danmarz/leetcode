# Write your MySQL query statement below
SELECT 
    id,
    MAX(CASE WHEN month = 'Jan' THEN revenue END) AS Jan_Revenue,
    MAX(CASE WHEN month = 'Feb' THEN revenue END) AS Feb_Revenue,
    MAX(CASE WHEN month = 'Mar' THEN revenue END) AS Mar_Revenue,
    MAX(CASE WHEN month = 'Apr' THEN revenue END) AS Apr_Revenue,
    MAX(CASE WHEN month = 'May' THEN revenue END) AS May_Revenue,
    MAX(CASE WHEN month = 'Jun' THEN revenue END) AS Jun_Revenue,
    MAX(CASE WHEN month = 'Jul' THEN revenue END) AS Jul_Revenue,
    MAX(CASE WHEN month = 'Aug' THEN revenue END) AS Aug_Revenue,
    MAX(CASE WHEN month = 'Sep' THEN revenue END) AS Sep_Revenue,
    MAX(CASE WHEN month = 'Oct' THEN revenue END) AS Oct_Revenue,
    MAX(CASE WHEN month = 'Nov' THEN revenue END) AS Nov_Revenue,
    MAX(CASE WHEN month = 'Dec' THEN revenue END) AS Dec_Revenue
FROM 
    Department
GROUP BY 
    id
ORDER BY 
    id;

-- SELECT
--     id,
--     `Jan` AS Jan_Revenue,
--     `Feb` AS Feb_Revenue,
--     `Mar` AS Mar_Revenue,
--     `Apr` AS Apr_Revenue,
--     `May` AS May_Revenue,
--     `Jun` AS Jun_Revenue,
--     `Jul` AS Jul_Revenue,
--     `Aug` AS Aug_Revenue,
--     `Sep` AS Sep_Revenue,
--     `Oct` AS Oct_Revenue,
--     `Nov` AS Nov_Revenue,
--     `Dec` AS Dec_Revenue
-- FROM (
--     SELECT id, month, revenue
--     FROM Department
-- ) AS src
-- PIVOT (
--     MAX(revenue)
--     FOR month IN (`Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, `Dec`)
-- ) AS pivot_table
-- ORDER BY id;



