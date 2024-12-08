# Write your MySQL query statement below
-- SELECT employee_id
-- FROM Employees
-- WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
-- UNION
-- SELECT employee_id
-- FROM Salaries
-- WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
-- ORDER BY employee_id ASC


-- Using NOT EXISTS is more performant versus NOT IN as the db engine does short-circuit evaluation,
-- and needs not maintain a virtual table with all employee_id's in memory. 
SELECT employee_id
FROM Employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM Salaries s
    WHERE s.employee_id = e.employee_id
)
UNION
SELECT employee_id
FROM Salaries s
WHERE NOT EXISTS (
    SELECT 1
    FROM Employees e
    WHERE e.employee_id = s.employee_id
)
ORDER BY employee_id ASC;
