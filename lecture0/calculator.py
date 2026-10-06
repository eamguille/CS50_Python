
# Asks the user for the value of x and y, and then converts those values into integers values
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# Asks the user for the value of a and b, and then converts those values into float values
a = float(input("What's a? "))
b = float(input("What's b? "))
print(a + b)

# Round Function - https://docs.python.org/3/builtins/functions.html#round
c = float(input("What's c? "))
d = float(input("What's d? "))
e = round(c + d)
print(f"{e:,}") # Formatting 1000 into 1,000

# Division
f = float(input("What's f? "))
g = float(input("What's g? "))
h = round((f / g), 2)
input(h) # We can also use format string and round the number by doing f"{h:.2f}"