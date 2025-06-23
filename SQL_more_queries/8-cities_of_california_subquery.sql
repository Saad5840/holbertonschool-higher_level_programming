-- Select the id and name of cities
SELECT id, name
FROM cities
-- Filter cities to only those whose state_id matches
-- the id of the state named 'California'
WHERE state_id = (
    -- Subquery to get the id of the state named 'California'
    SELECT id FROM states WHERE name = 'California'
)
-- Order results by city id in ascending order
ORDER BY id ASC;

