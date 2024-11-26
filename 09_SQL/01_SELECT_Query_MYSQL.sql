Select * from moviesdb.movies;
SELECT title, industry FROM moviesdb.movies;
USE moviesdb;
SELECT title, industry FROM movies;
# These upper four queries are same

SELECT * from movies where industry="Bollywood";
SELECT count(*) from movies where industry="Bollywood";
SELECT * from movies where industry="hollywood";
SELECT COUNT(*) from movies where industry="hollywood";
SELECT DISTINCT industry from movies;
SELECT * from movies where title LIKE "THOR%";
SELECT * from movies where title LIKE "%America%";
SELECT * FROM movies WHERE studio="";