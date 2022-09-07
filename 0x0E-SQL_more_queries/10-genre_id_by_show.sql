-- List all shows cobtained in `hbtn_0d_tvshows` that have atleast one genre linked
SELECT ts.`title`, tsg.`genre_id`  FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS tsg
ON ts.`id` = tsg.`show_id`
ORDER BY ts.`title`, tsg.`genre_id`;
