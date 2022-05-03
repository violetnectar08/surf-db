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
join wsl.region region on city.region_id = region.region_id
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

select * from wsl.tour;
select * from wsl.event;
select * from wsl.round;
select * from wsl.heat_details;
select * from wsl.heat_surfers;
select * from wsl.heat_results;
