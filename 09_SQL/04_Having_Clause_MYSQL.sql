# print all the years where more than 2 movies were released

select release_year, count(*) as movies_count
from movies
group by release_year
order by movies_count desc;

# error
select release_year, count(*) as movies_count
from movies
where movies_count>2
group by release_year
order by movies_count desc;

# having clause
select release_year, count(*) as movies_count
from movies
group by release_year
having movies_count>2
order by movies_count desc;

# where and having together
select release_year, count(*) as movies_count
from movies
where imdb_rating>6
group by release_year
having movies_count>2
order by movies_count desc;

