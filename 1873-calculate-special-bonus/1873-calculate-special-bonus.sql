# Write your MySQL query statement below
SELECT employee_id,
if (employee_id % 2 != 0 and name NOT LIKE 'M%', salary, 0) as bonus
FROM Employees order by employee_id;