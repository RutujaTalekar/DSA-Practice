# Write your MySQL query statement below

select * from Cinema where description  <> 'boring' and id % 2 != 0
order by rating desc;

-- Note - instead of using %, use mod(id, 2) = 1

