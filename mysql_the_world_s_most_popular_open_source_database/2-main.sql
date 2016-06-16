# Display the number of seasons from the TV shows in the database.
\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT t.name,
       count(t.name) AS nb_seasons
FROM Season AS s
LEFT JOIN TVShow AS t ON t.id = s.tvshow_id
GROUP BY t.name;

# Display the list of TV shows with their corresponding networks in alphabetical order.
\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT t.name AS 'TVShow name',
       n.name AS 'Network name'
FROM Network AS n
LEFT JOIN TVShow AS t ON t.network_id = n.id
ORDER BY t.name ASC;

# Display the list of TV shows on the network 'Fox (US)' in alphabetical order.
\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT t.name
FROM Network AS n
LEFT JOIN TVShow AS t ON t.network_id = n.id
WHERE (n.name = 'FOX (US)')
ORDER BY t.name ASC;

# Display the list of TV shows with the count of their episodes.
\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT t.name,
       count(t.name) AS nb_episodes
FROM Episode AS e
LEFT JOIN Season AS s ON e.season_id = s.id
LEFT JOIN TVShow AS t ON s.tvshow_id = t.id
GROUP BY t.name;
