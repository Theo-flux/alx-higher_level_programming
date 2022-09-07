-- Display the top 3 of cities temperature during July and August
-- Order by temperature (descending)
SELECT `city` , AVG(`value`) as avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg` DESC TOP 3;

