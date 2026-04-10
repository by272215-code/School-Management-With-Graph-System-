import matplotlib.pyplot as plt
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def display(self):
        super().display()
        print("Subject:", self.subject)
# Derived class: Student
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def display(self):
        super().display()
        print("Grade:", self.grade)
# Further derived class: ClassTeacher
class ClassTeacher(Teacher):
    def __init__(self, name, age, subject, class_assigned):
        super().__init__(name, age, subject)
        self.class_assigned = class_assigned
    def display(self):
        print("---- Class Teacher Details ----")
        super().display()
        print("Class Assigned:", self.class_assigned)
# Objects
t1 = Teacher("Rupesh sir", 30, "Mathematics")
s1 = Student("Bittu", 20, "B.tech CSE (AI & ML)")
ct1 = ClassTeacher("Raja sir", 25, "Python", "1A")
print("---- Teacher Details ----")
t1.display()
print("\n---- Student Details ----")
s1.display()
print()
ct1.display()

# 📊 GRAPH PART
names = [t1.name, s1.name, ct1.name]
ages = [t1.age, s1.age, ct1.age]
plt.figure()
plt.bar(names, ages)
plt.title("Age Comparison")
plt.xlabel("Persons")
plt.ylabel("Age")
plt.show()