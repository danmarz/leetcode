-- -- Works, but is inefficient
-- SELECT employee_id
-- FROM Employees
-- WHERE
--     salary < 30000 
--     AND manager_id NOT IN (SELECT employee_id FROM Employees)
-- ORDER BY employee_id

-- Optimized approach, using LEFT JOIN to find employees whose manager is not in the table

SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL -- Ensure employees have a manager
  AND m.employee_id IS NULL -- Manager has left
ORDER BY e.employee_id;
