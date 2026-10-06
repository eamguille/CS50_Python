# String methods works for manipulate strings for multiple purposes
# https://docs.python.org/3/builtins/stdtypes.html#string-methods

# Ask user for their name
name = input("What's your name? ")

# strip method removes whitespace from str
name = name.strip()

# Capitalize user's name
name = name.capitalize()

# Capitalize every single word in a text
name = name.title()

# Say hello to user
print(f"Hello, {name}")



"""
Those same blocks of code, can be simplified by doing this
"""

name1 = input("What's your name? ")
name1 = name1.strip().title()
print(f"Hello, {name1}")


"""
Or this 
"""

name2 = input("What's your name? ").strip().title()
print(f"Hello, {name2}")


# Split user's name into first name and last name
first, last = name.split(" ")
print(f"Hello, {first}") # It will print only the first name, because it will split the str until it finds the space character