# How many movies were released between 2015 and 2022
select count(*)
from movies 
where release_year between 2015 and 2022;

# Print the max and min movie release year
select max(release_year) as max_year,
min(release_year) as min_year
 from movies;

# Print a year and how many movies were released in that year starting with the latest year
select release_year,
count(*) as movies_count
from movies group by release_year order by release_year desc;