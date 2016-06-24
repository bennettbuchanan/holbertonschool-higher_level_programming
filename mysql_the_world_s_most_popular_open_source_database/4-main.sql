# Display all genres with their respective TV shows.
\! echo "\nList of all TVShows by all Genres ordered by genre name (A-Z)? (if a genre has 0 TVShow, please display NULL)"
SELECT g.name AS 'Genre name',
       t.name AS 'TVShow name'
FROM Genre AS g
LEFT JOIN TVShowGenre AS tg ON g.id = tg.genre_id
LEFT JOIN TVShow AS t ON t.id = tg.tvshow_id
ORDER BY g.name ASC;

# Display the name of the TV show with the corresponding pilot edisode.
\! echo "\nName of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)?"
SELECT t.name AS 'TVShow name',
       e.name AS 'Episode name'
FROM Episode AS e
LEFT JOIN Season AS s ON e.season_id = s.id
LEFT JOIN TVShow AS t ON t.id = s.tvshow_id
WHERE e.number = 1
    AND s.number = 1
ORDER BY t.name ASC;

# Display each TV show's respective genre.
\! echo "\nList of all Genres by all TVShows ordered by TVShow name (A-Z)? (if a genre has 0 TVShow, please display NULL as TVShow name)"
SELECT t.name AS 'TVShow name',
       g.name AS 'Genre name'
FROM Genre AS g
LEFT JOIN TVShowGenre AS tg ON g.id = tg.genre_id
LEFT JOIN TVShow AS t ON t.id = tg.tvshow_id
ORDER BY t.name ASC;
