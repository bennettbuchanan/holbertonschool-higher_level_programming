import time
import BaseHTTPServer
import mysql.connector
import json

HOST_NAME = 'localhost'
PORT_NUMBER = 9898

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        cnx = mysql.connector.connect(user='student',
                                      password='aLQQLXGQp2rJ4Wy5',
                                      host='173.246.108.142',
                                      database='Project_169')
        arr = []
        path_arr = s.path.split('/')
        cursor = cnx.cursor()

        if path_arr[1] == "tvshows":
            query = ("SELECT id, name, poster FROM TVShow GROUP BY name ASC;")
            cursor.execute(query)
            shows = cursor.fetchall()

            for i in shows:
                arr.append({'id': i[0], 'name': i[1], 'poster': i[2]})

        elif path_arr[1] == "tvshow" and len(path_arr) == 3:
            genre_arr = []
            query = ("SELECT t.id, t.name, t.poster, t.overview, n.name " +
                     "FROM TVShow AS t LEFT JOIN Network AS n " +
                     "ON t.network_id = n.id WHERE t.id = " +
                     path_arr[2] + ";")
            genre_query = ("SELECT g.name FROM TVShow AS t " +
                           "LEFT JOIN TVShowGenre AS tg " +
                           "ON tg.tvshow_id = t.id LEFT JOIN Genre AS g " +
                           "ON g.id = tg.genre_id WHERE t.id = " +
                           path_arr[2] + ";")
            cursor.execute(query)
            show = cursor.fetchall()
            cursor.execute(genre_query)
            genres = cursor.fetchall()

            for g in genres:
                genre_arr.append(g[0])

            for i in show:
                arr.append({'id': i[0], 'name': i[1], 'poster': i[2],
                            'overview': i[3], "network": i[4],
                            "genres": genre_arr})

        elif path_arr[1] == "tvshow" and path_arr[3] == "actors" and len(path_arr) == 4:
            query = ("SELECT a.id, a.name FROM Actor AS a LEFT JOIN " +
                     "TVShowActor AS ta ON a.id = ta.actor_id " +
                     "LEFT JOIN TVShow AS t ON ta.tvshow_id = t.id " +
                     "WHERE t.id = " + path_arr[2] + " ORDER BY a.name ASC;")
            cursor.execute(query)
            actor = cursor.fetchall()

            for i in actor:
                arr.append({'id': i[0], 'name': i[1]})

        elif path_arr[1] == "tvshow" and path_arr[3] == "seasons" and len(path_arr) == 4:
            query = ("SELECT id, number FROM Season WHERE tvshow_id = " +
                     path_arr[2] + " ORDER BY number;")
            cursor.execute(query)
            season = cursor.fetchall()

            for i in season:
                arr.append({'id': i[0], 'number': i[1]})

        elif path_arr[1] == "tvshow" and path_arr[3] == "season" and path_arr[5] == "episodes" and len(path_arr) == 6:
            query = ("SELECT e.id, e.number, e.name FROM Season AS s " +
                     "LEFT JOIN Episode AS e ON s.id = e.season_id " +
                     "WHERE s.tvshow_id = " + path_arr[2] +
                     " AND e.season_id = " + path_arr[4] + ";")
            cursor.execute(query)
            episodes = cursor.fetchall()

            for i in episodes:
                arr.append({'id': i[0], 'number': i[1], 'name': i[2]})

        elif path_arr[1] == "tvshow" and path_arr[3] == "season" and path_arr[5] == "episode" and len(path_arr) == 7:
            query = ("SELECT e.id, e.number, e.name, e.overview " +
                     "FROM Season AS s LEFT JOIN Episode AS e " +
                     "ON s.id = e.season_id WHERE s.tvshow_id = " +
                     path_arr[2] + " AND e.season_id = " + path_arr[4] +
                     " AND e.id = " + path_arr[6] + ";")
            cursor.execute(query)
            episode = cursor.fetchall()

            for i in episode:
                arr.append({'id': i[0], 'number': i[1], 'name': i[2],
                            'overview': i[3]})

        jsonObj = json.dumps(arr)
        s.wfile.write("%s" % jsonObj)
        cnx.close()

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
