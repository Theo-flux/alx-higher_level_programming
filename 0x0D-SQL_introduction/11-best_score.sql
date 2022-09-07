-- script that lists all records of the table second_table
-- Records of score greater than 10
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
