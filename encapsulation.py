# creating a class
class Employer:
  def __init__(self, employee_count):
    self._employee_count = employee_count # Private attribute (name mangling)

  def get_employee_count(self): # method
    return self._employee_count # Accessing private attribute via method

# creating an object
employer_one = Employer(1500)    

print("No. of Employees:", employer_one.get_employee_count())