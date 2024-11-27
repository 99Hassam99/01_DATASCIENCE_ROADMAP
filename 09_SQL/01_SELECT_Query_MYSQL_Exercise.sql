select * from movies;

# Print all movie titles and release year for all Marvel Studios movies.
select title,release_year from moviesdb.movies;

# Print all movies that have Avenger in their name.
select * from movies where title like "%Avenger%";

# Print the year when the movie "The Godfather" was released.
select release_year from movies where title="The Godfather";

# Print all distinct movie studios in the Bollywood industry.
select distinct studio from movies where industry="bollywood"