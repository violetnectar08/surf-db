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

-- events
select	tour.tour_name,
		event.event_name,
        event.stop_nbr,
        country.country,
        region.region,
        break.break_name,
        event.open_date,
        event.close_date
from wsl.event event
join wsl.tour tour
		on tour.tour_id = event.tour_id
join wsl.break break
		on break.break_id = event.break_id
join wsl.region region
		on region.region_id = break.region_id
join wsl.country country
		on country.country_id = region.country_id
;


-- heat details
select 	tour.tour_name,
		event.event_name,
        round.round,
        heat_details.heat_nbr,
		heat_details.wind,
        heat_details.heat_date,
        heat_details.duration,
        heat_details.wave_min,
        heat_details.wave_max
from wsl.heat_details heat_details
join wsl.event event
		on event.event_id = heat_details.event_id
join wsl.round round
		on round.round_id = heat_details.round_id
join wsl.tour tour
		on tour.tour_id = event.tour_id
;

-- surfers in heats
select 	tour.tour_name,
		event.event_name,
        round.round,
        heat_details.heat_nbr,
		surfers.full_name
from wsl.heat_surfers heat_surfers
join wsl.surfers surfers
		on surfers.surfer_id = heat_surfers.surfer_id
join wsl.heat_details heat_details
		on heat_details.heat_id = heat_surfers.heat_id
join wsl.event event
		on event.event_id = heat_details.event_id
join wsl.round round
		on round.round_id = heat_details.round_id
join wsl.tour tour
		on tour.tour_id = event.event_id
;

-- heat Results
select 	tour.tour_name,
		event.event_name,
        round.round,
        heat_details.heat_nbr,
        heat_results.surfer_in_heat_id,
		surfers.full_name,
        heat_results.status,
        heat_results.pick_to_win_percent,
        heat_results.jersey_color,
        heat_results.wave_1,
        heat_results.wave_2,
        heat_results.wave_3,
        heat_results.wave_4,
        heat_results.wave_5,
        heat_results.wave_6,
        heat_results.wave_7,
        heat_results.wave_8,
        heat_results.wave_9,
        heat_results.wave_10,
        heat_results.wave_11,
        heat_results.wave_12,
        heat_results.wave_13,
        heat_results.wave_14,
        heat_results.wave_15
from wsl.heat_results heat_results
join wsl.heat_surfers heat_surfers
		on heat_surfers.surfer_heat_id = heat_results.surfer_in_heat_id
join wsl.surfers surfers
		on surfers.surfer_id = heat_surfers.surfer_id
join wsl.heat_details heat_details
		on heat_details.heat_id = heat_results.heat_id
join wsl.event event
		on event.event_id = heat_details.event_id
join wsl.round round
		on round.round_id = heat_details.round_id
join wsl.tour tour
		on tour.tour_id = event.event_id
;

-- Count surfers in rounds
select tour.tour_name,
		event.event_name,
        round.round,
        count(distinct heat_surfers.surfer_id) as nbr_of_surfers
from wsl.heat_surfers heat_surfers
join wsl.surfers surfers
		on surfers.surfer_id = heat_surfers.surfer_id
join wsl.heat_details heat_details
		on heat_details.heat_id = heat_surfers.heat_id
join wsl.event event
		on event.event_id = heat_details.event_id
join wsl.round round
		on round.round_id = heat_details.round_id
join wsl.tour tour
		on tour.tour_id = event.event_id
group by tour_name, event_name, round
;
