# Write your MySQL query statement below
SELECT customer_id, SUM(CASE WHEN transaction_id IS NULL THEN 1 ELSE 0 END) AS count_no_trans
FROM Visits
LEFT JOIN Transactions USING (visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id

SELECT customer_id, COUNT(visit_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions USING (visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id

-- -- Step 1: Select all visit IDs and customer IDs from the Visits table
-- -- that do not have a matching visit_id in the Transactions table
-- SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
-- FROM Visits v
-- -- LEFT JOIN the Transactions table so that we can identify visits that have no transactions.
-- LEFT JOIN Transactions t
-- -- Match on the visit_id to see if the visit resulted in any transaction.
-- ON v.visit_id = t.visit_id
-- -- Step 2: Filter out rows where there was a transaction (i.e., transaction_id is not null).
-- WHERE t.transaction_id IS NULL
-- -- Step 3: Group by the customer_id to count the number of times each customer visited without a transaction.
-- GROUP BY v.customer_id
-- -- Step 4: Sort the result by customer_id or leave it unsorted since the problem does not specify a sort order.
-- ORDER BY v.customer_id;