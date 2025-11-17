class Person:
  def __init__(self, name):
   self.name=name
   
  def greet(self):
    print(f"hello, my name is {self.name}")
    
class Teacher(Person):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject
    
  def teach(self):
    print(f"{self.name} is teaching {self.subject}")
    
class Student(Person):
  def __init__(self, name, course):
    super().__init__(name)
    self.course = course
    
  def study(self):
    print(f"{self.name} is studying {self.course}")
    
p1 = Person('Erick')
p1.greet()
p2 = Person('Mercy')
p2.greet()
    
t1 = Teacher('Erick', 'Python programming')
t1.teach()

s1 = Student('Mercy', 'Django')
s1.study()            