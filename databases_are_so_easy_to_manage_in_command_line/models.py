from peewee import *

'''Create the SQLite database.'''
my_models_db = SqliteDatabase('my_models.db', pragmas=(('foreign_keys',
                                                        True),))


class BaseModel(Model):
    '''Define a BaseModel class for other tables to derive from.'''
    id = PrimaryKeyField(primary_key=True, unique=True)
    database = my_models_db

    class Meta:
        '''Define the database from which this class is created.'''
        database = my_models_db
        order_by = ('id', )


class School(BaseModel):
    name = CharField(128, null=False)

    def __str__(self):
        return "School: " + self.name + " (" + str(self.id) + ")"


class Batch(BaseModel):
    school = ForeignKeyField(School, related_name='batches',
                             on_delete='CASCADE')
    name = CharField(128, unique=True, null=False)

    def __str__(self):
        return "Batch: " + self.name + " (" + str(self.id) + ")"


class User(BaseModel):
    first_name = CharField(128, default="")
    last_name = CharField(128, null=False)
    age = IntegerField(null=False)

    def __str__(self):
        return "User: " + self.first_name + self.last_name + "(" + str(self.id) + ")"


class Student(User):
    batch = ForeignKeyField(Batch, related_name='students',
                            on_delete='CASCADE')

    def __str__(self):
        '''Add a space in front of first_name if it exists to return a properly
        spaced string.
        '''

        return "Student: " + self.first_name + " " + self.last_name + " (" + str(self.id) + ") " + "part of the batch: " + str(self.batch)


class Exercise(BaseModel):
    SUBJECTS = [('math', "Math"),
                ('english', "English"),
                ('history', "History"),
                ('c_prog', "C prog"),
                ('swift_prog', "Swift prog")]
    student = ForeignKeyField(Student, related_name='exercises',
                              on_delete='CASCADE')
    subject = CharField(128, default="", choices=SUBJECTS)
    note = IntegerField(default=0)

    def __str__(self):
        return "Exercise: " + str(self.student) + " has " + str(self.note) + " in " + self.subject + " (" + str(self.id) + ")"
