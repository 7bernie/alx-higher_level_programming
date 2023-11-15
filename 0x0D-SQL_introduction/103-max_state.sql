-- This script that lists all records with a score >= 10 in
-- the table second_table of the database hbtn_0c_0 in my MySQL server
SELECT state, MAX(value) AS max_temp 
FROM temperatures
GROUP BY state 
ORDER BY state;
