-- script that lists all records of the table second_table
-- Records are ordered by score field in desc order
UPDATE `score` FROM `second_table`
WHERE `name` = 'Bob';
