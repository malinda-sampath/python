print("hello 'world'")
print('hello "world"')


# This is a multiline string. It can span multiple lines.
a = """This is a 
multiline string."""
print(a)

print(a[0]) # prints the first character of the string

for i in "banana":
  print(i) # prints each character of the string

print(len(a)) # returns the length of the string

print("banana" in a) # returns True if "banana" is found in the string a
print("apple" not in a) # returns True if "apple" is NOT found in the string a

# String slicing
b = "Hello, World!" 
print(b[2:5]) # returns characters from index 2 to 5 (not included)
print(b[:5]) # returns characters from the beginning to index 5 (not included)
print(b[2:]) # returns characters from index 2 to the end

# Negative indexing
c = "Hello, World!"
print(c[-5:-2]) # returns characters from index -5 to -2 (not included)

# Modifying strings
d = "Hello, World!"
print(d.upper()) # returns the string in upper case
print(d.lower()) # returns the string in lower case
print(d.strip()) # returns the string with whitespace removed from the beginning and the end
print(d.replace("H", "J")) # returns the string with "H" replaced by "J"
print(d.split(",")) # returns a list where the text between the specified separator is the list items


# String concatenation
e = "Hello"
f = "World"

print(e+f) # returns "HelloWorld"
print(e + " " + f) # returns "Hello World"

# f-strings (formatted string literals)
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.") # returns "My name is John and I am 30 years old."
price = 49.99
print(f"The price is {price:.2f}") # returns "The price is 49.99" with 2 decimal places

