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

func print (p: Person) -> String {
    print(p.fullName())
    return p.fullName()
}

class Mentor: Person, Classify {
    let subject: Subject?
    init(first_name: String, last_name: String, age: Int, subject: Subject?) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age: age)
    }
    
    override convenience init(first_name: String, last_name: String, age: Int) {
        self.init(first_name: first_name, last_name: last_name, age: age, subject: Subject.English)
    }
    
    func isStudent() -> Bool {
        return false
    }
    
    func stringSubject() -> String {
        return subject!.rawValue
    }
}

class Student: Person, Classify {
    func isStudent() -> Bool {
        return true
    }
}

class School {
    var name: String
    var list_persons:[Person]

    init(name: String) {
        self.name = name
        self.list_persons = []
    }
    
    func addStudent(p: Person) -> Bool {
        if p is Student {
            list_persons.append(p)            
            return true
        } else {
            return false
        }
    }
    
    func addMentor(p: Person) -> Bool {
        if p is Mentor {
            list_persons.append(p)
            return true
        } else {
            return false
        }
    }
    
    func listStudents() -> [Person] {
        var arr = [Person]()
        for p in list_persons {
            if p is Student {
                arr.append(p)
            }
        }
        return arr.sort({ $0.age > $1.age })
    }
    
    func listMentors() -> [Person] {
        var arr = [Person]()
        for p in list_persons {
            if p is Mentor {
                arr.append(p)
            }
        }
        return arr.sort({ $0.age > $1.age })
    }
    
    func mentorsAgeAverge() -> Int {
        var average: Int = 0
        var i: Int = 0
        for p in list_persons {
            if p is Mentor {
                if let p = p as? Mentor {
                    average += p.age
                    i += 1
                }
            }
        }
        return average / i
    }
    
    func studentsAgeAverge() -> Int {
        var average: Int = 0
        var i: Int = 0
        for p in list_persons {
            if p is Student {
                if let p = p as? Student {
                    average += p.age
                    i += 1
                }
            }
        }
        return average / i
    }
    
    func listMentorsBySubject(subject: Subject) -> [Person] {
        var arr = [Person]()
        for p in list_persons {
            if p is Mentor {
                if let p = p as? Mentor {
                    if p.stringSubject() == String(subject) {
                        arr.append(p)
                    }
                }
            }
        }
        return arr.sort({ $0.age > $1.age })
    }
}

protocol Classify {
    func isStudent() -> Bool
}

enum Subject: String {
    case Math, English, French, History
}

