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
		on tour.tour_id = event.tour_id
group by tour_name, event_name, round
;

-- number of surfers in each heat
-- and number of surfers eliminated in each heat
select tour.tour_name,
		event.event_name,
        round.round,
        count(distinct heat_nbr) as nbr_of_heats,
        count(distinct heat_surfers.surfer_id) as nbr_of_surfers,
		sum(case when heat_results.status = 'Eliminated'
								then 1 else 0
										end) as nbr_surfers_elim
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
		on tour.tour_id = event.tour_id
where tour_name = '2022 Mens Championship Tour'
and event_name = 'Billabong Pro Pipe'
and round = 'Final'
group by tour_name, event_name, round
;
