--QUERY TO OBTAIN THE WHEATHER CONDITION ON TRIPS WITH MORE THAN 0 SECONDS AND ABOVE 0 MILES
select trip_start_timestamp, trip_end_timestamp, time, trip_seconds, trip_miles, weather, wind, visibility from chicago_taxi_dataset, weathercondition, trip_weather
where trip_id = unique_key
and weather_id = id
and trip_seconds > 0
and trip_miles > 0
order by 4 ASC

--Query to obtain the best company fare in one trip at november 2016 in Chicago
select company, trip_seconds, trip_miles, fare, (fare/trip_miles) as BestFare from chicago_taxi_dataset where trip_seconds <= 5400 and fare > 0 and trip_miles > 0 order by 5 ASC

