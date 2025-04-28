# Write your MySQL query statement below
select i.unique_id, e.name
from employees e left join employeeuni i
on i.id = e.id;

-- Note - Because I am using left join on id
-- employees without unique IDs will also be retained, 
-- but their corresponding columns from employee_uni will be filled with NaN 
-- (Not a Number) values.
