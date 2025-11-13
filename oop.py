# define a class
class Student:

  # define a constructor
  def __init__(self, name, score):
    self.name = name
    self.score = score
  
  # define method
  def display(self):
    print(f"Name: {self.name} score: {self.score}")

  # define a method to check if student passes
  def check_pass(self):
    return self.score >= 50
    
  # create objects
s1 = Student('Fraciah', 85)
s2 = Student('Erick', 40)   

s1.display()
print(f"Passed status: ", {s1.check_pass()})