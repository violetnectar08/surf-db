select * from wsl.continent;
select * from wsl.country;
select * from wsl.region;
select * from wsl.city;
select * from wsl.break;

-- cities
select	continent.continent,
		    country.country,
        region.region,
        city.city
from wsl.city city
join wsl.region region on break.region_id = region.region_id
join wsl.country country on region.country_id = country.country_id
join wsl.continent continent on continent.continent_id = country.continent_id

-- breaks
select	continent.continent,
		    country.country,
        region.region,
        break.break_name
from wsl.break break
join wsl.region region on city.region_id = region.region_id
join wsl.country country on region.country_id = country.country_id
join wsl.continent continent on continent.continent_id = country.continent_id


select * from wsl.surfers;

select 	gender,
		first_name,
        last_name,
        stance,
        rep_country.country as rep_country,
        current_date() - birthday as age,
        height,
        weight,
        concat(first_season, ' ', first_tour) as rookie_year,
        home_country.country as home_country,
        home_region.region as home_region,
        home_city.city as home_city
from wsl.surfers surfers
join wsl.country as rep_country
		on rep_country.country_id = surfers.rep_country_id
join wsl.city as home_city
		on home_city.city_id = surfers.home_city_id
join wsl.region as home_region
		on home_region.region_id = home_city.region_id
join wsl.country as home_country
		on home_country.country_id = home_region.country_id
;


select * from wsl.tour;
select * from wsl.event;
select * from wsl.round;
select * from wsl.heat_details;
select * from wsl.heat_surfers;
select * from wsl.heat_results;
