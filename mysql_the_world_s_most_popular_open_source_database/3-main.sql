# Display the TV show by name and filter by count of season quantity.
\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
SELECT t.name
FROM Season AS s
LEFT JOIN TVShow AS t ON t.id = s.tvshow_id
GROUP BY t.name
HAVING COUNT(t.name) > 3;

# Display all TV shows that have the genre 'Comedy', in alphabetical order.
\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
SELECT t.name
FROM TVShow AS t
LEFT JOIN TVShowGenre AS tg ON t.id = tg.tvshow_id
LEFT JOIN Genre AS g ON tg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY t.name ASC;

# Display actors on 'The Big Bang Theory', ordered alphabetically.
\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
SELECT a.name
FROM Actor AS a
LEFT JOIN TVShowActor AS ta ON a.id = ta.actor_id
LEFT JOIN TVShow AS ts ON ta.tvshow_id = ts.id
WHERE ts.name = 'The Big Bang Theory'
ORDER BY a.name ASC;

# Display the count of tvshow appearances per actor, in descending order.
\! echo "\nTop 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
SELECT a.name,
       count(ta.tvshow_id) AS nb_tvshows
FROM Actor AS a
LEFT JOIN TVShowActor AS ta ON a.id = ta.actor_id
GROUP BY a.name
ORDER BY nb_tvshows DESC LIMIT 10;
