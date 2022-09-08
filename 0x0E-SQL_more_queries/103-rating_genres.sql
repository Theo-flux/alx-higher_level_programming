-- list all genres in the database by their rating
SELECT tg.`name`, SUM(tsr.`rate`) AS `rating`
FROM `tv_genres` AS tg
INNER JOIN `tv_show_genres` AS tsg
ON tsg.`genre_id` = tg.`id`
INNER JOIN `tv_show_ratings` AS tsr
ON tsr.`show_id` = tsg.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
