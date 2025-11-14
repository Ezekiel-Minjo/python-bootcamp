# creating a class
class Employer:
  def __init__(self, name, industry):
    self.name = name # attribute
    self.industry = industry # attribute

  def display_info(self): # method
    print(f"Employer: {self.name} - {self.industry}")
    
# Creating an object
employer_one = Employer("Tpoint Tech", "Education")
employer_one.display_info()

