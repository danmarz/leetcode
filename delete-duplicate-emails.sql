# Write your MySQL query statement below
DELETE p1
FROM Person p1 
JOIN Person p2 ON p1.email = p2.email AND p1.id > p2.id

#DELETE FROM Person
#WHERE id IN (
#    SELECT p.id FROM (
#        SELECT t1.id
#        FROM Person t1
#        JOIN Person t2 ON t1.email = t2.email
#        WHERE t1.id > t2.id) p
#        )