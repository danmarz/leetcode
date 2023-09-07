# Write your MySQL query statement below
# 1.
#SELECT name AS Customers
#FROM Customers
#LEFT JOIN Orders ON Customers.id = Orders.customerId
#WHERE customerID IS NULL;

# 2.
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
);