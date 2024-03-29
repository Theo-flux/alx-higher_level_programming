-- Display the avergae temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT `city`, AVG(`VALUE`) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
