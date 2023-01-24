"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
It also accepts camel, pascal and snake case
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


#Python allows you to assign values to multiple variables in one line:
print("")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:
print("")

a = b = c = "Orange"

print(a)
print(b)
print(c)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
print("")


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)