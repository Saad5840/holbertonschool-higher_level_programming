-- Select the city id, city name, and state name
SELECT cities.id, cities.name, states.name
FROM cities
-- Join states table to get the corresponding state name for each city
JOIN states ON cities.state_id = states.id
-- Order results by city id in ascending order
ORDER BY cities.id ASC;
