# while loop
num = 0

while num <= 15:
  print(f"Loop: {num}")
  num+=6

# for loop
students = ['minjo', 'kevin', 'brian', 'joan', 'Ombachi', 'Flavian', 'Lilian', 'Felix']
print(students)
for name in students:
  print(name[6])

x = "Mr. Minjo"
for i in x:
  print(i)

# sum of numbers in a list
numbers = [10, 24, 17, 29, 30, 46, 21, 8, 19]
total = 0
for el in numbers:
  total +=el
print(f"The sum of the numbers is {total}")  