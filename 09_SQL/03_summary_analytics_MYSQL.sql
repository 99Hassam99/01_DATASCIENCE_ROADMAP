# MAX imdb rating for bollywood movies
select MAX(imdb_rating) from movies where industry='bollywood';

# Min imdb rating for bollywood movies
select MIN(imdb_rating) from movies where industry='bollywood';

# Average rating of marvel movies
select avg(imdb_rating) from movies where studio='Marvel Studios';
# Decreasing the decimal points
select round(avg(imdb_rating),2) from movies where studio='Marvel Studios';
# defining custom header names
select round(avg(imdb_rating),2) as avg_rating
 from movies where studio='Marvel Studios';
# defining min max avg colum name for marvel studios
select min(imdb_rating) as min_rating,
max(imdb_rating) as max_rating, 
round(avg(imdb_rating),2) as avg_rating
 from movies where studio='Marvel Studios';

# counting fucntion
select count(*) from movies where industry='bollwood';

# group-by function for industry
select industry,
count(*) from movies
Group by industry;

# group-by function for studio
select studio,
count(*) from movies
Group by studio;

# the upper query is in random order but
# we can make it in some specified order as
select studio,
count(*) as cnt from movies
Group by studio
order by cnt desc;

# movie count and the average rating
select industry,
count(industry) as cnt,
avg(imdb_rating) as avg_rating
from movies
group by industry;

# rounding decimal
select industry,
count(industry) as cnt,
round(avg(imdb_rating),2) as avg_rating
from movies
group by industry;

# for studio
select studio,
count(studio) as cnt,
round(avg(imdb_rating),2) as avg_rating
from movies
group by studio
order by avg_rating DESC;

# skipping null values
select studio,
count(studio) as cnt,
round(avg(imdb_rating),2) as avg_rating
from movies
where studio!=''
group by studio
order by avg_rating DESC;
