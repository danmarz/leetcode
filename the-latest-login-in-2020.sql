# Write your MySQL query statement below
SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
-- WHERE time_stamp LIKE "2020-%"
-- Range filtering is generally faster
WHERE time_stamp >= '2020-01-01' -- Start of 2020
  AND time_stamp < '2021-01-01'  -- End of 2020 (exclusive) 
GROUP BY user_id;
