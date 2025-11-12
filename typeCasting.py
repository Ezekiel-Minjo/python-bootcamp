# initializing variables
num_1 = 12 # init
num_2 = 3.6 # float
res = num_1 + num_2 # resultant value is a float
print(res, "=>", type(res))

# type casting in python is classified into two types
#  1. Implicit Type Casting - python interpreter automaticaly converts one data type into another without user intervention.
#  2. Explicit Type Casting - user manually converts a variable's data type by using built-in capabilities.

# Implicit Type Casting, or Type Coercion
# int->float->complex
#  Precision loss means losing the exactness or accuracy of a number when it’s converted from one data type to another.

# simple programs to show impilicit type casting

# initializing variables
a = 5 # int
b = 7.6 # float
c = 3 + 4j # complex

# impilicit type casting
d = a + b # impilicit conversion; int -> float
e = a + b + c # implicit conversion: int -> complex
print(d, '=>', type(d))
print(e, '=>', type(e))