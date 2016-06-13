import sys
import json
from peewee import *
from decimal import *
from models import BaseModel, School, Batch, User, Student, Exercise

classes = {"school": School,
           "batch": Batch,
           "student": Student,
           "exercise": Exercise}

mean = [{"subject": "Math", "pts_total": 0.0, "num": 0, "mean": 0.0},
        {"subject": "English", "pts_total": 0.0, "num": 0, "mean": 0.0},
        {"subject": "History", "pts_total": 0.0, "num": 0, "mean": 0.0},
        {"subject": "C prog", "pts_total": 0.0, "num": 0, "mean": 0.0},
        {"subject": "Swift prog", "pts_total": 0.0, "num": 0, "mean": 0.0}]


def print_item(argv):
    '''Iterate through the classes with the corresponding classes and print the
    item when found.
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
        exercise = Exercise.create(student=argv[3],
                                   subject=argv[4],
                                   note=argv[5])
        print "New Exercise: " + str(exercise)


def create_item():
    '''Creates the database with the appropriate tables.'''
    table_arr = []
    for k in classes:
        table_arr.append(classes.get(k))

    BaseModel.database.connect()
    BaseModel.database.create_tables(table_arr)


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
    for batch in Batch.select():
        if str(batch.id) == str(argv[2]):
            return
    print "School not found"


def print_student_by_school(argv):
    '''Takes the system arguments as parameter and then prints the students
    based on the student id. Prints 'School not found' if the id does not
    exist.

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
    '''Print all data in database, ordered with tab heirarchy.

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
                            if exercise.student.id == student.id:
                                print "\t\t\t" + str(exercise)


def get_average(exercise, argv):
    '''Find the averages of the exercises given.

    Keyword arguments:
    argv -- An array of command line arguments.
    exercise -- The exercise object in which to factor in the average.
    '''
    for i in range(0, len(mean)):
        if mean[i].get("subject") == exercise.subject:
            mean[i]["num"] += 1
            mean[i]["pts_total"] += exercise.note
    for i in range(0, len(mean)):
        if mean[i]["num"] > 0:
            mean[i]["mean"] = mean[i][
                "pts_total"] / mean[i]["num"]


def print_averages(item, print_items=True):
    '''Print the averages based on a the mean dict or return the averages if
    print_items is False.

    Keyword arguments:
    i -- An item of the mean dict.
    print_items -- Boolean value to optionally print the values
    '''
    average_dict = {}
    if mean[item]["num"] > 0:
        '''Remove decimal place if an int.'''
        if mean[item]["mean"] % 1 == 0:
            if print_items is True:
                print mean[item]["subject"] + ":",
                print str("%g" % mean[item]["mean"])
            else:
                average_dict["subject"] = mean[item]["subject"]
                average_dict["average"] = ("%g" % mean[item]["mean"])
                return average_dict
        else:
            if print_items is True:
                print mean[item]["subject"] + ":",
                print str(round(mean[item]["mean"], 5))
            else:
                average_dict["subject"] = mean[item]["subject"]
                average_dict["average"] = round(mean[item]["mean"], 5)
                return average_dict


def handle_average(argv, Class, class_str, call_print_averages=True):
    '''Pass the appropriate data to get the corresponding averages.

    Keyword arguments:
    argv -- An array of command line arguments.
    Class -- The class in which to find the averages.
    class_str -- The stringified Classname (e.g., a Student class would be
    "Student").
    call_print_averages -- Boolean value to optionally print the averages
    '''
    arr = []
    for i in mean:
        i["pts_total"] = 0.0
        i["mean"] = 0.0
        i["num"] = 0
    for exercise in Exercise.select():
        compare = {"Student": exercise.student.id,
                   "Batch": exercise.student.batch.id,
                   "School": exercise.student.batch.school.id}
        if str(compare.get(class_str)) == str(argv[2]):
            get_average(exercise, argv)
    for i in range(0, len(mean)):
        if call_print_averages is True:
            print_averages(i)
        else:
            if print_averages(i, False) is not None:
                arr.append(print_averages(i, False))
    for student in Class.select():
        if str(student.id) == str(argv[2]):
            return arr
    print class_str + " not found"


def note_average_by_student(argv):
    '''Print the average of a student's score in each field.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    handle_average(argv, Student, "Student")


def note_average_by_batch(argv):
    '''Print the average of a batch's score in each field.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    handle_average(argv, Batch, "Batch")


def note_average_by_school(argv):
    '''Print the average of a school's score in each field.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    handle_average(argv, School, "School")


def top_batch(argv):
    '''Print the student object that is the top of a given batch.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    top = {"score": 0.0, "student": Student}

    for student in Student.select():
        if str(student.batch.id) == str(argv[2]):
            arr = handle_average(["", "", student.id], Student,
                                 "Student", False)
            for dict in arr:
                dict["student"] = student
            if len(argv) > 3:
                for i in arr:
                    if i["subject"] == argv[3]:
                        if i["average"] > top["score"]:
                            top["score"] = i["average"]
                            top["student"] = i["student"]
            else:
                for i in arr:
                    if i["average"] > top["score"]:
                        top["score"] = i["average"]
                        top["student"] = i["student"]
    print top["student"]


def top_school(argv):
    '''Print the student object that is the top of a given school.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    top = {"score": 0.0, "student": Student}

    for student in Student.select():
        if str(student.batch.school.id) == str(argv[2]):
            arr = handle_average(["", "", student.id], Student,
                                 "Student", False)
            for dict in arr:
                dict["student"] = student
            for i in arr:
                if i["average"] > top["score"]:
                    top["score"] = i["average"]
                    top["student"] = i["student"]
    print top["student"]


def import_json(argv):
    '''Import data from a JSON string. Must be a valid JSON string with the
    respective data fields.

    Keyword arguments:
    argv -- An array of command line arguments.
    '''
    try:
        loaded_json = json.loads(argv[2])
    except ValueError, e:
        print "Please set a JSON string"
        return
    try:
        int(argv[2])
        print "Please set a JSON string"
        return
    except ValueError, e:
        batch_id = 0
        student_id = 0
        for k in loaded_json:
            for batch in k["batches"]:
                for student in batch["students"]:
                    for exercise in student["exercises"]:
                        insert_item(["", "insert", "school", k["name"]])
                        for school in School.select():
                            if school.name == k["name"]:
                                school_id = school.id
                        insert_item(["", "insert", "batch", school_id,
                                     batch.get("name")])
                        for orig_batch in Batch.select():
                            if orig_batch.name == batch.get("name"):
                                batch_id = orig_batch.id
                        insert_item(["", "insert", "student", batch_id,
                                     student.get("age"),
                                     student.get("last_name"),
                                     student.get("first_name")])
                        for s in Student.select():
                            if s.first_name == student.get("first_name"):
                                student_id = s.id
                        insert_item(["", "insert", "exercise", student_id,
                                     exercise.get("subject"),
                                     exercise.get("note")])


def export_json(argv):
    '''Export all data in JSON format.

    Keyword arguments:
    argv -- An array of command line arguments.
    '''
    data = []
    for school in School.select():
        dict = {"name": school.name}
        data.append(dict)

    '''Add the batches.'''
    for dict in data:
        batches = []
        for batch in Batch.select():
            if batch.school.name == dict["name"]:
                batch_dict = {}
                dict["batches"] = batches
                batch_dict["name"] = batch.name
                batches.append(batch_dict)

    '''Add the students in their batch.'''
    for dict in data:
        if dict.get("batches") is not None:
            for batch in dict.get("batches"):
                students = []
                for student in Student.select():
                    if str(student.batch.name) == str(batch["name"]):
                        student_dict = {}
                        batch["students"] = students
                        student_dict["first_name"] = student.first_name
                        student_dict["last_name"] = student.last_name
                        student_dict["age"] = student.age
                        students.append(student_dict)

    '''Add the exercises to the corresponding student.'''
    for dict in data:
        if dict.get("batches") is not None:
            for batch in dict.get("batches"):
                for student in batch["students"]:
                    exercises = []
                    for e in Exercise.select():
                        if e.student.first_name == student.get("first_name"):
                            exercsie_dict = {}
                            student["exercises"] = exercises
                            exercsie_dict["note"] = e.note
                            exercsie_dict["subject"] = e.subject
                            exercises.append(exercsie_dict)

    print json.dumps(data)


actions = {"create": create_item,
           "print": print_item,
           "insert": insert_item,
           "delete": delete_item,
           "print_batch_by_school": print_batch_by_school,
           "print_student_by_batch": print_student_by_batch,
           "print_student_by_school": print_student_by_school,
           "print_family": print_family,
           "age_average": age_average,
           "change_batch": change_batch,
           "print_all": print_all,
           "note_average_by_student": note_average_by_student,
           "note_average_by_batch": note_average_by_batch,
           "note_average_by_school": note_average_by_school,
           "top_batch": top_batch,
           "top_school": top_school,
           "export_json": export_json,
           "import_json": import_json}


def handle_action(argv):
    '''Takes the system arguments as parameter and then handles the actions
    based on the model class definitions.

    Keyword arguments:
    argv -- An array of command line arguments passed to the program.
    '''
    if argv[1] == "create":
        if len(argv) == 3 and argv[2] == "test":
            print "create"
        else:
            create_item()
    else:
        for k in actions:
            if argv[1] == k:
                actions.get(k)(argv)


'''Interpret the command line. Handle the action, if possible.'''
if len(sys.argv) == 1:
    print "Please enter an action"
else:
    if sys.argv[1] in actions:
        handle_action(sys.argv)
    else:
        print "Undefined action " + sys.argv[1]
