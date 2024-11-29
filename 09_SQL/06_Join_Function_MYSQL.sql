# inner join 
select 
m.movie_id, title, budget, revenue,currency,unit
from movies m
join financials f # it is by default inner join
on m.movie_id=f.movie_id;

# left join 
select 
m.movie_id, title, budget, revenue,currency,unit
from movies m
left join financials f 
on m.movie_id=f.movie_id;

# right join 
select 
f.movie_id, title, budget, revenue,currency,unit
from movies m
right join financials f 
on m.movie_id=f.movie_id;

# full join
select 
m.movie_id, title, budget, revenue,currency,unit
from movies m left join financials f on m.movie_id=f.movie_id

UNION

select 
f.movie_id, title, budget, revenue,currency,unit
from movies m right join financials f on m.movie_id=f.movie_id;

# right outer join 
select 
m.movie_id, title, budget, revenue,currency,unit
from movies m
right outer join financials f 
on m.movie_id=f.movie_id;

# left outer join 
select 
m.movie_id, title, budget, revenue,currency,unit
from movies m
left outer join financials f 
on m.movie_id=f.movie_id;

# USING clause left
select 
movie_id, title, budget, revenue,currency,unit
from movies m
left join financials f 
USING (movie_id);

# USING clause right
select 
movie_id, title, budget, revenue,currency,unit
from movies m
right join financials f 
USING (movie_id);