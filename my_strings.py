# method 1: using triple quotes ()
str_1 = '''Learning Python
is fun with
Tpoint Tech'''

str_2 = """ Tpoint Tech is
the best place to learn
Python Programming """

# print("Multiline String 1:")
# print(str_1)
# print()
# print("Multiline String 1:")
# print(str_2)

# Accessing Characters in a String
# given string
s = "Tpoint Tech"
# print("Given String: ", s)
# accessing characters using indexing
# print("s[0]=", s[0])
# print("s[9]=", s[9])
# Accessing String with Negative Indexing
# print("s[-1]=", s[-1])
# print("s[-6]=", s[-6])

# String Slicing
# getting characters from index 1 to 4: 'poin' 
# print("s[1:5] =", s[1:5])

# getting characters from beginning to index 3: 'Tpoi' 
# print("s[:4] =", s[:4])

# getting characters from index 4 to end: 'nt Tech' 
# print("s[4:] =", s[4:])

# reversing a string: 'hceT tniopT'
# print("s[::-1] =", s[::-1])

# String Immutability
# given string
msg = "tpointtech"
print("Given String:", msg)
msg = "T" + msg[1:6] + " T" + msg[7:]
print("New String:", msg)
# Deleting a String
del msg
# print(msg)

# Updating a String
# given string
given_str = "welcome learners"
print("Given String:", given_str)

# updating a string by creating a new one
new_str_1 = "W" + given_str[1:]

# replacing "learners" with " to Tpoint Tech"
new_str_2 = given_str.replace("learners", "to Tpoint Tech")

# print results
print("New String 1:", new_str_1)
print("New String 2:", new_str_2)

# Common String Methods
# len()

# given string
given_str = "tpointtech"
print("Given String:", given_str)

# using len() function
num_of_chars = len(given_str)
print("Number of Characters:", num_of_chars)

# upper() and lower()
given_str = "Tpoint Tech"
print("Given String:", given_str)

# using the upper() method
print("Uppercase String:", given_str.upper())
# using the lower() method
print("Lowercase String:", given_str.lower())

# Note: Strings are immutable; therefore, all of these methods will return a new string, keeping the original one unchanged.

# Formatting Strings : ways to include variables inside strings
# using f-strings
name = "Ezekiel"
age = 23
city = "Nairobi"

# using f-strings
print(f"{name} is a {age} years old boy living in {city} city")

# using format()
name = "Sachin"
profession = "Software Developer"
company = "Apple Inc"

# using the format() method
msg = '{} is a {} at {}.'.format(name, profession, company)
print(msg)\

# String Membership Test: test if a substring exists within a string or not using 'in' and 'not in' keywords
given_str = 'Tpoint Tech'

print(f"Does 'p' exist in '{given_str}'?", 'p' in given_str)
print(f"Does 'e' exist in '{given_str}'?", 'e' not in given_str)