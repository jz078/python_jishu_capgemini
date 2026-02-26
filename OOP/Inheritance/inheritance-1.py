class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

# hierarchical inheritance
class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno


# multiple inheritance
class Academic:
    def __init__(self, course = None, cgpa = None):
        self.course = course
        self.cgpa = cgpa 

class Sports:
    def __init__(self, sport_name = None, level = None):
        self.sport_name = sport_name
        self.level = level

# Hybrid Inheritance
class AllRounderStudent(Student, Academic, Sports):
    def __init__(self, name, age, rollno, is_academic = False, is_sports = False, 
                course = None, cgpa = None, sport_name = None, level = None):
        super().__init__(name, age, rollno)
        self.is_academic = is_academic
        self.is_sports = is_sports 

        if self.is_academic:
            Academic.__init__(self, course, cgpa)

        if self.is_sports:
            Sports.__init__(self, sport_name, level)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll no: {self.rollno}")

        if self.is_academic:
            print(f"Course: {self.course}")
            print(f"CGPA: {self.cgpa}")

        if self.is_sports:
            print(f"Sport name: {self.sport_name}")
            print(f"Sport Level: {self.level}")



# @ Academic Student 
s1 = AllRounderStudent('Aman', 22, 101, is_academic=True, course='CSE', cgpa=6.7)
s1.display()