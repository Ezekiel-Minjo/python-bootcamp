num = int(input("Enteer a number: "))

if num%2 == 0:
  print(f"{num} is an even number")
else:
  print(f"{num} is an odd number")

# if elif else statement

marks = int(input("Enter your marks: "))

if marks >= 80  and marks <= 100:
  print(f"{marks} is an A")
elif marks >= 79  and marks <= 60:
  print(f"{marks} is a B")
elif marks >= 59 and marks <= 50:
  print(f"{marks} is a C")
elif marks >= 49 and marks <= 40:
  print(f"{marks} is a D")
elif marks >= 39 and marks <= 30:
  print(f"{marks} is a E")
else:
  print(f"{marks} is a F")