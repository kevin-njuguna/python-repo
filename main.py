#class variables - shared among all instances of a class
# defined outside the constructor
# allow you to share data among all objects created from that class

class Student:
    
   class_year = 2030
   num_students = 0
    
   def __init__(self, name, age):
      self.name = name
      self.age = age
      Student.num_students += 1
      
student1 = Student("Maureen",  19)
student2 = Student("Fridah",  20)

print(student1.name)
#print(student2.class_year)
print(Student.class_year)
print(Student.num_students)