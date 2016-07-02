from peewee import *
from playhouse.fields import ManyToManyField

'''Create the SQLite database.'''
my_models_db = SqliteDatabase(None)


class BaseModel(Model):
    '''Define a BaseModel class for other tables to derive from.'''
    id = PrimaryKeyField(primary_key=True, unique=True)
    database = my_models_db

    class Meta:
        '''Define the database from which this class is created.'''
        database = my_models_db
        order_by = ('id', )


class FilmModel(BaseModel):
    '''Class of film from Star Wars API.'''
    title = CharField(128, null=False)
    release_date = CharField(128, null=False)
    episode_id = IntegerField(null=False)


class PeopleModel(BaseModel):
    '''Class of a character from Star Wars API.'''
    name = CharField(128, null=False)
    films = ManyToManyField(FilmModel, related_name='characters')


class PlanetModel(BaseModel):
    '''Class of planet from Star Wars API.'''
    name = CharField(128, null=False)
    climate = CharField(128, null=False)
    residents = ManyToManyField(PeopleModel, related_name='homeworld')
    films = ManyToManyField(FilmModel, related_name='planets')
