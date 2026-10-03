# Ask user for their name
name = input("What's your name? ")


# Say hello to user
print("hello, " + name)
print("hello,", name)

# Handle end parameter in print function - docs.python.org - https://docs.python.org/3/builtins/functions.html#print
print("Hello, ", end="")
print(name)

# Handle separator parameter in print function - docs.python.org
print("Hello,", name, sep=":::")


# Putting quotation marks inside the quotation marks
print('Hi! "friend"')
print("Hi! \"friend\"") # Technique called Escaping


# The most used and elegant way to concatenate many strings in a print function
print(f"Hi, {name}") # It's called format string