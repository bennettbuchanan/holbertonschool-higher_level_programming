import mysql.connector

cnx = mysql.connector.connect(user='student', password='aLQQLXGQp2rJ4Wy5',
                              host='173.246.108.142',
                              database='Project_169')

cursor = cnx.cursor()

show_data = ("SELECT name FROM TVShow GROUP BY name ASC;")
cursor.execute(show_data)
shows = cursor.fetchall()

for name in shows:
    print name[0] + ":"
    season_data = ("SELECT s.number, s.id FROM Season AS s LEFT JOIN TVShow AS t ON s.tvshow_id = t.id WHERE t.name = " + "'" + name[0] + "'" + ";")
    cursor.execute(season_data)
    seasons = cursor.fetchall()
    for num in seasons:
        print "\tSeason" + str(num[0]) + ":"
        episode_data = ("SELECT number, name FROM Episode WHERE season_id = " + str(num[1]) + ";")
        cursor.execute(episode_data)
        episodes = cursor.fetchall()
        for episode in episodes:
            print "\t\t" + str(episode[0]) + ": " + episode[1]

cnx.close()
