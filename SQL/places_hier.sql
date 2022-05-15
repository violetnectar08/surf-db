-- ID Tables
select * from wsl.continent;
select * from wsl.country;
select * from wsl.region;
select * from wsl.city;
select * from wsl.break;

-- Countries
select 	continent.continent,
		country.country
from wsl.country country
join wsl.continent continent
		on country.continent_id = continent.continent_id
order by continent, country
;



-- Regions
select 	continent.continent,
		country.country,
		region.region
from wsl.region region
join wsl.country country
		on country.country_id = region.country_id
join wsl.continent continent
		on continent.continent_id = country.continent_id
order by continent, country, region
;

-- breaks
select	continent.continent,
		    country.country,
        region.region,
        city.city
from wsl.city city
join wsl.region region on city.region_id = region.region_id
join wsl.country country on region.country_id = country.country_id
join wsl.continent continent on continent.continent_id = country.continent_id
order by continent, country, region, city
;
