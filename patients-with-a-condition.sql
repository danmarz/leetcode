# Write your MySQL query statement below
SELECT 
    patient_id, 
    patient_name, 
    conditions
FROM 
    Patients
WHERE 
    conditions LIKE 'DIAB1%'   -- DIAB1 is at the beginning
    OR conditions LIKE '% DIAB1%' -- DIAB1 is preceded by a space
    OR conditions LIKE '% DIAB1'  -- DIAB1 is at the end with a preceding space
    OR conditions = 'DIAB1';   -- DIAB1 is the only condition