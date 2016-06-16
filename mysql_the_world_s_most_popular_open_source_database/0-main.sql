# Show the non-temporary tables in the database.
\! echo "\nList of all tables?"
SHOW TABLES;

\! echo "\nDisplay the table structure of TVShow, Genre and TVShowGenre?"
# Show the CREATE TABLE statement that creates a TVShow.
SHOW CREATE TABLE TVShow;

# Show the CREATE TABLE statement that creates a Genre.
SHOW CREATE TABLE Genre;

# Show the CREATE TABLE statement that creates a TVShowGenre.
SHOW CREATE TABLE TVShowGenre;

# Display a list of TVShow names with their id in ascending order.
\! echo "\nList of TVShows, only id and name ordered by name (A-Z)?"
SELECT id,
       name
FROM TVShow
GROUP BY name ASC;

# Display a list of Genre names with their id in descending order.
\! echo "\nList of Genres, only id and name ordered by name (Z-A)?"
SELECT id,
       name
FROM Genre
GROUP BY name DESC;

# List all networks by id and name.
\! echo "\nList of Network, only id and name?"
SELECT id,
       name
FROM Network;

# Display the number of edisodes (i.e., rows) in the Episode table.
\! echo "\nNumber of episodes in the database?"
SELECT count(id)
FROM Episode;
