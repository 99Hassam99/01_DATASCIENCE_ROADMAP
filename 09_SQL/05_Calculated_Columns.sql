# CurDate/Current date
SELECT CURDATE();
# current year only
SELECT YEAR(CURDATE());

select * from actors;

# ACTORS AND YEAR
select *,YEAR(CURDATE()) from actors;

# Age of actors
select *,YEAR(CURDATE())-birth_year as age from actors;

# Financial table
select * from financials;

# profit
SELECT *, (revenue-budget) as profit from financials;

# profit in one currency
SELECT *, 
if(currency="USD",revenue*84.50,revenue) as revenue_inr
 from financials;
 
# unit conversion
select distinct unit from financials;

# CASE Statement
select *,
CASE
	WHEN unit='thousands' THEN revenue/1000
	WHEN unit='billions' THEN revenue*1000
	WHEN unit='millions' THEN revenue
END as revenue_mln
from financials;