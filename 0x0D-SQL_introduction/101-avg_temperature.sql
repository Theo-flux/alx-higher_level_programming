-- Display the avergae temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT `CITY`, AVG(*) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `VALUE` DESC;
