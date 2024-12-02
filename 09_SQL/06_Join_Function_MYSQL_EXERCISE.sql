#Write SQL queries for the following,
#1. Show all the movies with their language names
select m.title, l.name from movies m
Join languages l using (language_id);

#2. Show all Telugu movie names (assuming you don't know the language id for Telugu)
select title from movies m
left join languages l
on m.language_id=l.language_id
where l.name='Telugu';
#3. Show the language and number of movies released in that language
select
	l.name,
    count(m.movie_id) as no_movies
from languages l
left join movies m using (language_id)
group by language_id
order by no_movies DESC;