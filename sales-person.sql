# Write your MySQL query statement below

# Using Join
ELECT s.name FROM SalesPerson s 
	WHERE s.sales_id NOT IN (
		SELECT o.sales_id FROM Orders o LEFT JOIN Company c 
			ON c.com_id=o.com_id 
		WHERE c.name="RED"
	);
    
# Not using Join
 SELECT name FROM SalesPerson 
	 WHERE sales_id NOT IN(
		 SELECT sales_id FROM Orders WHERE com_id IN (
				 SELECT com_id FROM Company WHERE name="RED" )
	 );