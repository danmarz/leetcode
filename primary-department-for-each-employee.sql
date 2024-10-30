# Write your MySQL query statement below
-- Step 1: Select all employees who have a primary department assigned
SELECT 
    employee_id,                -- Select the employee ID
    department_id               -- Select the department ID of the primary department
FROM Employee
WHERE primary_flag = 'Y'        -- Only include rows where the department is marked as primary ('Y')

-- Step 2: Combine results with employees who do not have a primary department
UNION                           -- Use UNION to combine the results of both queries, removing duplicates

-- Step 3: Select employees who do not have any primary department ('Y') assigned
SELECT 
    employee_id,                -- Select the employee ID
    department_id               -- Select the department ID, which will be the only department for these employees
FROM Employee
WHERE employee_id NOT IN (      -- Exclude employees who already have a primary department
    SELECT employee_id          -- Subquery to get IDs of employees who have at least one primary department
    FROM Employee
    WHERE primary_flag = 'Y'    -- Filter to include only rows with a primary department ('Y')
);