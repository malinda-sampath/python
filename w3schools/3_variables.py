x = 5
y = "hello"

print(x)
print(y)

x = "Now I am a string"
y = 6

print(x)
print(y)

z = int(y) + 10

print (type(x))
print (type(y))

_my_var = "This is a variable with an underscore"

a, b, c = 1, 2, "Three"

a = b = c = 10

fruits = ["apple", "banana", "cherry"]

x , y, z = fruits


#  The global keyword is used to create a global variable inside a function.

n = "I am global"

def my_function():
    n = "I am inside the function"
    print(n)

    n = "I am local"
    print(n)

my_function()

def my_function2():
    global m
    m = "I am global m"

my_function2()

print(m)


