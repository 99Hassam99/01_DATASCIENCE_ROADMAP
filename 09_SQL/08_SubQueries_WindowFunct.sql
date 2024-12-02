# Subqueries in SQL are another way to achieve similar results as CTEs.
# They allow you to nest a query inside another query. 
# Subqueries can be used in the SELECT, FROM, or WHERE clauses, 
# and they are executed first, with their results passed to the outer query.

# Filter Movies Released After 2010
# Using a subquery in the FROM clause:
select * from movies, financials;
SELECT *
FROM (
    SELECT title, revenue, release_year
    FROM movies,financials
    WHERE release_year > 2010
) AS MoviesAfter2010;

# top grossing movie
SELECT revenue
FROM financials
WHERE revenue = (
    SELECT MAX(revenue)
    FROM financials
);

# Window function
# rank by revenue
SELECT 
    revenue,
    RANK() OVER (ORDER BY revenue DESC) AS rd
FROM financials;

# top grossing movies 

WITH RankedMovies AS (
    SELECT
        revenue,
        ROW_NUMBER() OVER (ORDER BY revenue DESC) AS row_num
    FROM financials
)
SELECT revenue
FROM RankedMovies
WHERE row_num <= 40; -- Top 3 movies

# average financials
SELECT 
    revenue,
    AVG(revenue) OVER () AS avg_financials
FROM financials;

# commulative financials
SELECT 
    revenue,
    SUM(revenue) OVER (ORDER BY revenue DESC) AS cumulative_financials
FROM financials;

# percentage
SELECT 
    revenue,
    ROUND((revenue * 100.0) / SUM(revenue) OVER (), 2) AS percentage_contribution
FROM financials;
