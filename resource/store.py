
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# students = []
students = reload() # recreate the list of Student objects from a file
s = Student("siti", 26)
students.append(s)
save(students) # save the list of Student objects or save all Student objects to a file