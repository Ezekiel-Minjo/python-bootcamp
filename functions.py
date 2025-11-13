def myfunction():
  print("This is my first function")
myfunction()
print()

def welcome(name):
  print(f"Hello, {name}! Welcome to Tpoint Tech!!")
welcome("Minjo")
print()

# funtions with parameters
def students(name, age, gender):
  print(f"student name is {name}")
  print(f"student age is {age}")
  print(f"student gender is {gender}")
students("minjo", 23, "Male") 
print()

# funtion with return values
def add_numbers(a, b):
  return  a + b
result = add_numbers(3, 9)