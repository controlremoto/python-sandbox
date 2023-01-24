x = 5
y = "John"
print(x)
print(y)

#Variables can change its type
print("")
x = 4       # x is of type int
print("Initial X value:",x)
x = "Sally" # x is now of type str
print("X value after change its type to string:",x)

#If you want to specify the data type of a variable, this can be done with casting.
print("")
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print("The X Value:",x)
print("The X Value:",y)
print("The X Value:",z)

print("Can any of above be changed?")
print("Y type BEFORE change",type(y))
y = "Foo"
print("Y type AFTER change",type(y))

print("The y value after change its type to string:",y)

#You can get the data type of a variable with the type() function.
print("")

x = 5
y = "John"
print(type(x))
print(type(y))

#String variables can be declared either by using single or double quotes:
print("")

x = "John"
# is the same as
x = 'John'

#Variable names are case-sensitive.
print("")

a = 4
A = "Sally"
#A will not overwrite a
print(A)
print(a)