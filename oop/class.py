class Student:

    year = 1
    num_of_students = 0

    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
        Student.num_of_students += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

s1 = Student('Alessandro', 'Versace', 'aleversace98@gmail.com')
s2 = Student('Me', "NotMe", "menotme@gmail.com")

print(s1.fullname())
print('\n')

print(s2.__dict__)
print('\n')

print(Student.__dict__)
s1.year = 2
print('\n')

print(s1.__dict__)
print('\n')

print(Student.num_of_students)