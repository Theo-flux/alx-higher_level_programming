-- List all shows, and all genres linked to that show, from the database.
SELECT ts.`title`, tg.`name`
FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS tsg
ON ts.`id` = tsg.`show_id`
INNER JOIN `tv_genres` AS tg
ON tg.`id` = tsg.`genre_id`
ORDER BY ts.`title`, tg.`name`;
