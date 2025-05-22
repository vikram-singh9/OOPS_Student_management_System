class Student:
    def __init__(self,name, roll):
        self.name = name
        self.roll = roll
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_Average(self):
        if len(self.grades) == 0:
            return 0
        return sum (self.grades) / len(self.grades)
        
    def display_info(self):
        print(f"Name: {self.name} Roll: {self.roll} average: {self.get_Average()} grades: {self.grades} ")



class School:
    def __init__(self):
        self.students = []

    def add_Student(self, student):
        self.students.append(student)

    def show_all_Students(self):
        for student in self.students:
            student.display_info()

# creating instances of the Student class
s1 = Student('Vikram', 230)
s2 = Student('Rahul', 390)
s3 = Student('Ravi', 120)

s1.add_grade(90)
s1.add_grade(89)

s2.add_grade(78)
s2.add_grade(33)

s3.add_grade(45)
s3.add_grade(67)
s3.add_grade(89)

school = School()
school.add_Student(s1)
school.add_Student(s2)
school.add_Student(s3)

school.show_all_Students()