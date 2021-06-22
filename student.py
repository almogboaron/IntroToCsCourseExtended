class Student:
    def __init__(self, name, surname, ID):
        self.name = name
        self.surname = surname
        self.id = ID
        self.grades = dict()

    def __repr__(self):  # must return a string
        return "<" + self.name + ", " + str(self.id) + ">"

    def update_grade(self, course, grade):
        self.grades[course] = grade

    def avg(self):
        s = sum([self.grades[course] for course in self.grades])
        return s / len(self.grades)

    def __eq__(self, other):
        assert isinstance(other, Student)
        return self.id == other.id

##s1 = Student("Hillary", "Clinton", 123456789)
##print(s1)
##s1.update_grade("CS1001", 91)
##print(s1.grades)
##s1.update_grade("HEDVA", 90)
##s1.update_grade("CS1001", 98) #she appealed
##print(s1.grades)
##print(s1.avg())
##
##s2 = Student("Angela", "Merkel", 888888888)
##s2.update_grade("Algebra1", 95)
##s2.update_grade("CS1001", 100)
##print(s2)
##print(s2.grades)
##print(s2.avg())

