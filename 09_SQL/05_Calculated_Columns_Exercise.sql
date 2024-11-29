# Write SQL queries for the following,
# Print profit % for all the movies

select *,
(((revenue-budget)*100)/revenue) as Profit
 from financials;
 
 select*,
 (revenue-budget) as profit,
 (revenue-budget)*100/budget as profit_per
 from financials;