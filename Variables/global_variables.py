# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, 
#this variable will be local, and can only be used inside the function. 
#The global variable with the same name will remain as it was, global and with the original value.


y = "awesome"

def myNewfunc():
    y = "fantastic"
    print("Python is " + y)

myNewfunc()

print("Python is " + y)

#To create a global variable inside a function, you can use the global keyword.
print("")

def myfuncB():
  global x
  x = "fantastic"

myfuncB()

print("Python is " + x)