class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname 
        print("Person created.")
    
    def who_am_i(self):
        print("I am a person.")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
    def who_am_i(self):
        print(f'I am {self.branch} teacher.')

class Student(Person): # Student,Person'ın alt sınıfıdır.
    def __init__(self, fname, lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print('Student created.')
    # Override
    def who_am_i(self):
        print("I am a student.")

p1 = Person('ali','yılmaz')
s1 = Student('çınar','yılmaz',1234)
t1 = Teacher('Ahmet','Can','Math')
print(f'name: {p1.firstName}, last name: {p1.lastName}')
print(f'name: {s1.firstName}, last name: {s1.lastName}, number: {s1.studentNumber}')

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()