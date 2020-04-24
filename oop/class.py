class Student:

    year = 1
    num_of_students = 0

    def __init__(self, first, last, email):     # Costruttore   self è la referenza all'oggetto stesso (this di Java)
        self.first = first
        self.last = last
        self.email = email
        Student.num_of_students += 1
        
    def fullname(self):         # Metodo
        return '{} {}'.format(self.first, self.last)    # self MUST be used

s1 = Student('Alessandro', 'Versace', 'aleversace98@gmail.com')
s2 = Student('Me', "NotMe", "menotme@gmail.com")

print(s1.fullname())
print('\n')

print(s2.__dict__)
print('\n')

print(Student.__dict__)
print('\n')

s1.year = 2
print(s1.__dict__) 
print('\n')

print(Student.num_of_students)

# Interfaces: methods with "visibility" outside the object.

# Encapsulation: restrict access of some components (Then we can control access with methods ie. get() and set())

# Inheritance: Sub-Classes inherit attributes and methods from their "parents" Classes (Super Classes).
# A Super class, B sub-class -> We say "B extends A".
# Can be single or multiple.

