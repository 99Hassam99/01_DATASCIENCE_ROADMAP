SELECT * FROM movies;
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
# By default it is in ascending order
SELECT * FROM movies Where industry='bollywood' ORDER BY imdb_rating;
# Descending order
SELECT * FROM movies Where industry='bollywood' ORDER BY imdb_rating desc;

# By default it is always in ascending order but we can use ascending order command

SELECT * FROM movies Where industry='bollywood' ORDER BY imdb_rating asc;

# To retrieve top rated movies for bollywood
SELECT * FROM movies Where industry='bollywood' ORDER BY imdb_rating DESC LIMIT 5;

# To retrieve top rated movies for hollywood
SELECT * FROM movies Where industry='hollywood' ORDER BY imdb_rating DESC LIMIT 5;
# skipping the 1st index i-e 0 index
SELECT * FROM movies Where industry='hollywood' ORDER BY imdb_rating DESC LIMIT 5 OFFSET 1;