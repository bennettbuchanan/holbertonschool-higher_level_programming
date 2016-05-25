class Person {
    var first_name: String
    var last_name: String
    var age: Int
    init(first_name: String, last_name: String, age: Int) {
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }
    
    func fullName() -> String {
        return self.first_name + " " + self.last_name
    }
}

class Mentor: Person, Classify {
    let subject: Subject
    init(first_name: String, last_name: String, age: Int, subject: Subject?) {
        self.subject = subject!
        super.init(first_name: first_name, last_name: last_name, age: age)
    }
    func isStudent() -> Bool {
        return false
    }
    func stringSubject() -> String {
        return self.subject.rawValue
    }
}

class Student: Person, Classify {
    func isStudent() -> Bool {
        return true
    }
}

class School {
    var name: String
    init(name: String) {
        self.name = name
    }
    var list_persons = [Person]()
    
    func addStudent(p: Person) -> Bool {
        if String(p.self) != "Student" {
            return false
        } else {
            list_persons.append(p)
            return true
        }
    }
    func addMentor(p: Person) -> Bool {
        if String(p.self) != "Mentor" {
            return false
        } else {
            list_persons.append(p)
            return true
        }
    }
    func listStudents() -> [Person] {
        var arr = [Person]()
        for p in list_persons {
            if String(p.self) == "Student" {
                arr.append(p)
            }
        }
        return arr
    }
    func listMentors() -> [Person] {
        var arr = [Person]()
        for p in list_persons {
            if String(p.self) == "Mentor" {
                arr.append(p)
            }
        }
        return arr
    }
    func listMentorsBySubject(subject: Subject) -> [Person] {
        let subject: Subject
        var arr = [Person]()
        for p in list_persons {
            if String(p.self) == "Mentor" {
                arr.append(p)
            }
        }
        return arr
    }
}

protocol Classify {
    func isStudent() -> Bool
}

enum Subject: String {
    case Math, English, French, History
}


var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
var m = Mentor(first_name: "Alex", last_name: "Rap", age: 34, subject: Subject.French)
var m2 = Mentor(first_name: "Gus", last_name: "Fring", age: 54, subject: Subject.English)
var m3 = Mentor(first_name: "Walter", last_name: "White", age: 52, subject: Subject.Math)


var school = School(name: "Holberton")
school.addStudent(s)
school.addMentor(m)
school.addMentor(m2)
school.addMentor(m3)

var students = school.listStudents()
for student in students
{
    print("Student: \(student.fullName())")
}
var mentors = school.listMentors()
for mentor in mentors
{
    print("Mentor: \(mentor.fullName())")
}

var mentors_math = school.listMentorsBySubject(Subject.Math)
for mentor_math in mentors_math
{
    print("Mentor Math: \(mentor_math.fullName())")
}

