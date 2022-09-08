-- List all show without the genre  `Comedy` int the database `hbtn_0d_tvshows`
SELECT DISTINCT(ts.`title`) FROM `tv_shows` AS ts
LEFT JOIN `tv_show_genres` AS tsg
ON ts.`id` = tsg.`show_id`
LEFT JOIN `tv_genres` AS tg
ON tg.`id` = tsg.`genre_id`
WHERE ts.`title` NOT IN (
SELECT ts.`title` FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS tsg
ON ts.`id` = tsg.`genre_id`
INNER JOIN `tv_genres` AS tg
ON tg.`id` = tsg.`show_id`
WHERE tg.`name` = 'Comedy')
ORDER BY ts.`title`;
