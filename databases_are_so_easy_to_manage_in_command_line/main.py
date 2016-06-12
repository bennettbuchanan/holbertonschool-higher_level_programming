import sys
from peewee import *
from models import BaseModel, School, Batch, User, Student, Exercise

classes = {"school": School,
           "batch": Batch,
           "student": Student,
           "exercise": Exercise}


def print_data(argv):
    '''Iterate through the classes with the corresponding classes and print the
    item, when found.
    '''
    if len(argv) > 2:
        for k in classes:
            if argv[2] == k:
                for item in classes.get(k).select():
                    print item


def delete_item(argv):
    '''Takes the system arguments as parameter and then deletes the item.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    for k in classes:
        if argv[2] == k:
            i = 0
            this_class = classes.get(k)
            '''
            Iterate through the database to search for corresponding id.
            '''
            for item in this_class.select():
                if str(item.id) == str(argv[3]):
                    print "Delete: " + str(item)
                    d = this_class.delete().where(this_class.id == item.id)
                    d.execute()
                i += 1
            if i == len(this_class.select()):
                print "Nothing to delete"


def insert_item(argv):
    '''Takes the system arguments as parameter and then inserts the item.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    if argv[2] == "school":
        school = School.create(name=argv[3])
        print "New school: " + str(School.get(School.name == argv[3]))
    elif argv[2] == "batch":
        batch = Batch.create(school=argv[3], name=argv[4])
        print "New batch: " + str(Batch.get(Batch.name == argv[4]))
    elif argv[2] == "student":
        print "New student:",
        if len(argv) > 6:
            student = Student.create(batch=argv[3],
                                     age=argv[4],
                                     last_name=argv[5],
                                     first_name=argv[6])
            print str(Student.get(Student.age == argv[4] and
                                  Student.last_name == argv[5] and
                                  Student.first_name == argv[6]))
        else:
            student = Student.create(batch=argv[3],
                                     age=argv[4],
                                     last_name=argv[5])
            print str(Student.get(Student.age == argv[4] and
                                  Student.last_name == argv[5]))
    elif argv[2] == "exercise":
        print "New Exercise: "


def create_item():
    '''Creates the database with the appropriate tables.'''
    table_arr = []
    for k in classes:
        table_arr.append(classes.get(k))

    BaseModel.database.connect()
    BaseModel.database.create_tables(table_arr, safe=True)


def print_batch_by_school(argv):
    '''Takes the system arguments as parameter and then prints the batch based
    on the school id. Prints 'School not found' if the id does not exist.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    i = 0
    for item in Batch.select():
        if str(item.school.id) == str(argv[2]):
            print item
            break
        i += 1
    if i == len(Batch.select()):
        print "School not found"


def print_student_by_batch(argv):
    '''Takes the system arguments as parameter and then prints the students
    in that batch based on the student id. Prints 'School not found' if the id
    does not exist.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    i = 0
    for student in Student.select().where(Student.batch == argv[2]):
        print student
    for item in Batch.select():
        if str(item.school.id) == str(argv[2]):
            break
        i += 1
    if i == len(Batch.select()):
        print "School not found"


def print_student_by_school(argv):
    '''Takes the system arguments as parameter and then prints the students
    based on the student id. Prints 'School not found' if the id does not exist.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    i = 0
    # for student in Student.select().where(Student.school.id == argv[2]):
    for student in Student.select():
        if str(student.batch.school.id) == str(argv[2]):
            print student
    for item in School.select():
        if str(item.id) == str(argv[2]):
            break
        i += 1
    if i == len(School.select()):
        print "School not found"


def print_family(argv):
    '''Takes the system arguments as parameter and then prints the students
    if their last name is that passed as argv[2]. Prints 'Last name not found'
    if the last name does not exist.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    found = False
    for student in Student.select():
        if str(student.last_name) == str(argv[2]):
            print student
            found = True
    if found is False:
        print "Last name not found"


def age_average(argv):
    '''Takes the system arguments as parameter and then prints the average age
    of all students. argv[2] is optionally a Batch id.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    sum = 0
    if len(argv) == 2:
        for student in Student.select():
            sum += student.age
    if len(argv) == 3:
        for student in Student.select().where(Student.batch == argv[2]):
            sum += student.age
    if sum > 0:
        print sum / len(Student.select())
    else:
        print "Cannot average age. There are no students in this batch"


def change_batch(argv):
    '''Takes the system arguments as parameter. argv[2] is id of the student to
    change, argv[3] is the batch to change the student to.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    student_found = False
    batch_found = False
    for student in Student.select():
        if str(student.id) == str(argv[2]):
            student_found = True
    for batch in Batch.select():
        if str(batch.id) == str(argv[3]):
            batch_found = True
    if student_found is False:
        print "Student not found"
        return
    if batch_found is False:
        print "Batch not found"
        return

    for student in Student.select():
        if str(student.id) == str(argv[2]):
            if str(student.batch.id) == str(argv[3]):
                student_found = True
                print student,
                print "already in " + str(student.batch)
            else:
                '''If the student is not already in the batch, then reassign.'''
                tmp_id = student.id
                tmp_age = student.age
                tmp_first_name = student.first_name
                tmp_last_name = student.last_name

                d = Student.delete().where(Student.id == tmp_id)
                d.execute()
                new = Student.create(id=tmp_id,
                                     batch=argv[3],
                                     age=tmp_age,
                                     last_name=tmp_last_name,
                                     first_name=tmp_first_name)

                print student,
                print "has been move to",
                print new.batch


def print_all(argv):
    '''Function description.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    for school in School.select():
        print school
        for batch in Batch.select():
            if batch.school.id == school.id:
                print "\t" + str(batch)
                for student in Student.select():
                    if student.batch.id == batch.id:
                        print "\t\t" + str(student)
                        for exercise in Exercise.select():
                            print "\t\t\t" + str(exercise)
                            print "Exercise printed!"

actions = {"create": create_item,
           "print": print_data,
           "insert": insert_item,
           "delete": delete_item,
           "print_batch_by_school": print_batch_by_school,
           "print_student_by_batch": print_student_by_batch,
           "print_student_by_school": print_student_by_school,
           "print_family": print_family,
           "age_average": age_average,
           "change_batch": change_batch,
           "print_all": print_all}


def handle_action(argv):
    '''Takes the system arguments as parameter and then handles the actions
    based on the model class definitions.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    for k in actions:
        if argv[1] == k:
            if k == "create":
                create_item()
            else:
                actions.get(k)(argv)

    # if argv[1] == "create":
    #     create_item()
    # elif argv[1] == "print":
    #     if len(argv) > 2:
    #         print_data(argv[2])
    # elif argv[1] == "insert":
    #     insert_item(argv)
    # elif argv[1] == "delete":
    #     delete_item(argv)
    # elif argv[1] == "print_batch_by_school":
    #     print_batch_by_school(argv)
    # elif argv[1] == "print_student_by_batch":
    #     print_student_by_batch(argv)
    # elif argv[1] == "print_student_by_school":
    #     print_student_by_school(argv)
    # elif argv[1] == "print_family":
    #     print_family(argv)
    # elif argv[1] == "age_average":
    #     age_average(argv)


'''Interpret the command line. Handle the action, if possible.'''
if len(sys.argv) == 1:
    print "Please enter an action"
else:
    if sys.argv[1] in actions:
        handle_action(sys.argv)
    else:
        print "Undefined action " + sys.argv[1]
