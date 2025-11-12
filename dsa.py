# list data structure
fruits = [ 'banana', 'mangoes', 'oranges', 'apples']
fruits.sort()
print(fruits)
fruits[1] = 'pineapples'
print(f'I like eating {fruits[1]}')
# a list is ordered, indexed, changeable, 

# tuple datastructures
cars = ('mercedes', 'nissan', 'Toyota', 'mazda')
print(cars)
print(f'{cars[0]} are manufuctured in Germany')
#  a tuple are ordered, allow duplicate , unchangeable and indexed

# set data structure
majina = { 'Erick', 'ivy', 'michael', 'mercy', 'mercy', 'jeremy'}
majina.add('antony')

print(majina)
# sets are unordered, does not allow duplicate, you can add data

# dictionary data structure
staff = { 'Name': 'Ezekiel', 'Age': 24, 'Gender': "Male"}
print(f"staff name is {staff['Name']} and staff age is {staff['Age']}")

# dict have a key value pairs