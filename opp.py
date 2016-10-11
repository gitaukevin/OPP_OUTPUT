class College(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized College: {})'.format(self.name))

    def tell(self):
        
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Lecturer(College):
    
    def __init__(self, name, age, salary):
        College.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Lecturer: {})'.format(self.name))

    def tell(self):
        College.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Learner(College):
    
    def __init__(self, name, age, marks):
        College.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Leaner: {})'.format(self.name))

    def tell(self):
        College.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

lec= Lecturer('Mrs. Wanjiku', 25, 25000)
stu = Leaner('Daniel', 16, 50)


print()

faculty = [lec, stu]
for member in faculty:
    
    member.tell()
