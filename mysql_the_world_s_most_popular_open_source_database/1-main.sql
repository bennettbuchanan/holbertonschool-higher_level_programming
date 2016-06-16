# Count the number of unique ids in the Season table.
\! echo "\nNumber of seasons by tvshow_id?"
SELECT tvshow_id,
       count(id)
FROM Season
GROUP BY tvshow_id;

# Count the number of unique ids that share the same episode number.
\! echo "\nNumber of occurrences of the same episode number ordered by episode number?"
SELECT number,
       count(id)
FROM Episode
GROUP BY number;

# Display the top three most occuring genres in all TV shows.
\! echo "\nTop 3 of the Genre's occurrences in all TVShows ordered by this number?"
SELECT genre_id,
       count(*) AS occurances_genre
FROM TVShowGenre
GROUP BY genre_id
ORDER BY occurances_genre DESC LIMIT 3;

# Display all TV shows with the letter sequence 'th' (case insensitive), and
# downcase the name of the TV show, if any characters are upper case.
\! echo "\nSearch all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?"
SELECT LOWER(name) as name
FROM TVShow
WHERE name LIKE '%th%';
