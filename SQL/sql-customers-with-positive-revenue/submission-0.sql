-- Write your query below
select customer_id
from customers
where revenue>0 and year in (2020);