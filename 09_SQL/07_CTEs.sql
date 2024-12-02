# CTE ( common table expression)
# A CTE is a temporary result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement. It's defined using the WITH keyword.

select * from movies;

WITH MoviesAfter2010 AS (
    SELECT title, industry, release_year
    FROM movies
    WHERE release_year > 2010
)
SELECT *
FROM MoviesAfter2010;



select * from financials;
# Top 3 highest-grossing movies
WITH RankedMovies AS (
    SELECT movie_id, revenue,
			RANK() OVER (ORDER BY revenue DESC) as BOC
    FROM financials
)
SELECT *
FROM RankedMovies
WHERE BOC <= 3;


WITH FinancialSummary AS (
    SELECT SUM(revenue) AS total_revenue, COUNT(*) AS total_movies
    FROM financials
)
SELECT total_revenue, total_movies
FROM FinancialSummary;
