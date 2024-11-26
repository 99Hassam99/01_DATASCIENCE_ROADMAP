SELECT * FROM movies WHERE imdb_rating>=9;
SELECT * FROM movies WHERE imdb_rating>9;
SELECT * FROM movies WHERE imdb_rating<7;
SELECT * FROM movies WHERE imdb_rating>=6 AND imdb_rating<=8;
# same function can be used as
SELECT * FROM movies WHERE imdb_rating BETWEEN 6 AND 8;

SELECT * FROM movies WHERE release_year=2022 or release_year=2019 or release_year=2018;
# Same function can be used as
SELECT * FROM movies WHERE release_year IN(2022,2019,2018);
# for text queries results
SELECT * FROM movies WHERE studio IN("Marvel Studios", "Zee Studios");
# Null values
SELECT * FROM movies WHERE imdb_rating is NULL;
# Not Null
SELECT * FROM movies WHERE imdb_rating is NOT NULL;
# print all movies with imdb_rating
SELECT * FROM movies Where industry='bollywood' ORDER BY imdb_rating