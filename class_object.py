class Person:
  def __init__(self, name, age):
    # This is the contructor method that is called when creating a new Person object
    # It takes two parameters, name, and age, and initializes them as attributes of the objects
    self.name = name
    self.age = age

  def greet(self):
    # This is a method of the Person class that prints a greeting message
    print("Hello, my name is " + self.name)  

# creating a new instance of the Person class and assign it to the variable person1
person1 = Person("Ayan", 25)
person1.greet()
