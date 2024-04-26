# Write your MySQL query statement below

# JOIN ... USING ...
SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project
JOIN Employee USING (employee_id)
GROUP BY project_id;

# JOIN ... ON ...
# SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_experience_years
# FROM Project p
# JOIN Employee e ON p.employee_id = e.employee_id
# GROUP BY p.project_id;