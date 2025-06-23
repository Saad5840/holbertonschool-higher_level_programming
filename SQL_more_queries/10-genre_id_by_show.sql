-- Select the tv show title and the associated genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Join tv_show_genres to link shows with their genres
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
-- Order by show title ascending, then genre_id ascending
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
