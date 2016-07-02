from peewee import *
import threading
import requests
import json
from h_swapi_models import BaseModel, FilmModel, PeopleModel, PlanetModel


class SWAPI(object):
    def __init__(self, database_name):
        '''SWAPI class which generates threads to create the database.

        Keyword arguments:
        database_name -- The string with which to name the database.
        '''
        self.__database_name = database_name
        self.__model_arr = [FilmModel, PeopleModel,
                            PeopleModel.films.get_through_model(),
                            PlanetModel,
                            PlanetModel.residents.get_through_model(),
                            PlanetModel.films.get_through_model()]

        BaseModel.database.init(self.__database_name)
        BaseModel.database.connect()
        BaseModel.database.create_tables(self.__model_arr)

    def start(self):
        '''Starts the concurrent threads to add rows to the database's tables.
        '''
        for i in range(1, 8):
            thread = FilmThread("http://swapi.co/api/films/" + str(i))
            FilmThread.thread_list += [thread]
            thread.start()

        for thread in FilmThread.thread_list:
            thread.join()

        for film in FilmModel.select().order_by(FilmModel.release_date):
            FilmThread.ordered_arr.append(film)

        CharactersThread.id_list = set(CharactersThread.id_list)

        for i in CharactersThread.id_list:
            thread = CharactersThread("http://swapi.co/api/people/" + str(i))
            CharactersThread.thread_list += [thread]
            thread.start()

        for thread in CharactersThread.thread_list:
            thread.join()

        PlanetThread.id_list = set(PlanetThread.id_list)

        for i in PlanetThread.id_list:
            thread = PlanetThread("http://swapi.co/api/planets/" + str(i))
            PlanetThread.thread_list += [thread]
            thread.start()

        for thread in PlanetThread.thread_list:
            thread.join()

        return

    def stop(self):
        '''Set the threading.Event() to true for each thread to stop the
        process.
        '''
        for thread in FilmThread.thread_list:
            thread.stop()

        for thread in CharactersThread.thread_list:
            thread.stop()

        for thread in PlanetThread.thread_list:
            thread.stop()

        BaseModel.database.close()

    def is_done(self):
        '''Method to determine when all threads are complete. Returns False if
        a thread is still in in process, and True otherwise.'''
        for thread in FilmThread.thread_list:
            if thread.is_alive() is True:
                return False

        for thread in CharactersThread.thread_list:
            if thread.is_alive() is True:
                return False

        for thread in PlanetThread.thread_list:
            if thread.is_alive() is True:
                return False

        return True


class FilmThread(threading.Thread):
    def __init__(self, url):
        '''A thread for adding an item to a table in the database.

        Keyword arguments:
        url -- The url to get data for a film from the Star Wars API.
        '''
        threading.Thread.__init__(self)
        self.__url = url
        self.__stop = threading.Event()

    thread_list = []
    ordered_arr = []

    def stop(self):
        '''Set the threading.Event() to true for each thread to stop the
        process.
        '''
        self.__stop.set()

    def run(self):
        '''Defines the threads activity. Makes a row in the FilmModel table
        with the corresponding data pulled from a request to the Star Wars API.
        '''
        data = requests.get(self.__url)
        obj = json.loads(data.text)
        FilmModel.create(title=str(obj.get("title")),
                         release_date=str(obj.get("release_date")),
                         episode_id=str(obj.get("episode_id")))

        for c in obj.get("characters"):
            c = c.split("/")
            character_id = c[-2]
            CharactersThread.id_list.append(str(character_id))

        for c in obj.get("planets"):
            c = c.split("/")
            planet_id = c[-2]
            PlanetThread.id_list.append(str(planet_id))


class CharactersThread(threading.Thread):
    def __init__(self, url):
        '''A thread for adding an item to a table in the database.

        Keyword arguments:
        url -- The url to get data for a character from the Star Wars API.
        '''
        threading.Thread.__init__(self)
        self.__url = url
        self.__stop = threading.Event()

    id_list = []
    thread_list = []

    def stop(self):
        '''Set the threading.Event() to true for each thread to stop the
        process.
        '''
        self.__stop.set()

    def run(self):
        '''Defines the threads activity. Makes a row in the PeopleModel table
        with the corresponding data pulled from a request to the Star Wars API.
        '''
        id = self.__url.split("/")
        data = requests.get(self.__url)
        obj = data.json()
        films_arr = obj.get("films")

        PeopleModel.create(id=id[-1], name=obj.get("name").encode("utf-8"))

        character = PeopleModel.get(PeopleModel.id == id[-1])

        for film in films_arr:
            this_id = film.split("/")
            this_id = this_id[-2]
            character.films.add(FilmThread.ordered_arr[int(this_id) - 1])


class PlanetThread(threading.Thread):
    def __init__(self, url):
        '''A thread for adding an item to a table in the database.

        Keyword arguments:
        url -- The url to get data for a planet from the Star Wars API.
        '''
        threading.Thread.__init__(self)
        self.__url = url
        self.__stop = threading.Event()

    id_list = []
    thread_list = []

    def stop(self):
        '''Set the threading.Event() to true for each thread to stop the
        process.
        '''
        self.__stop.set()

    def run(self):
        '''Defines the threads activity. Makes a row in the PlanetModel table
        with the corresponding data pulled from a request to the Star Wars API.
        '''
        id = self.__url.split("/")
        data = requests.get(self.__url)
        obj = data.json()
        films_arr = obj.get("films")
        residents_arr = obj.get("residents")

        PlanetModel.create(id=id[-1], name=obj.get("name").encode("utf-8"),
                           climate=obj.get("climate"))

        planet = PlanetModel.get(PlanetModel.id == id[-1])

        for film in films_arr:
            this_id = film.split("/")
            this_id = this_id[-2]
            planet.films.add(FilmThread.ordered_arr[int(this_id) - 1])

        for resident in residents_arr:
            this_id = resident.split("/")
            this_id = this_id[-2]
            planet_res = PeopleModel.select().where(PeopleModel.id == this_id)
            planet.residents.add(planet_res)
