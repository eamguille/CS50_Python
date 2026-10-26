
"""
i = 0
while i < 3:
    print("meow")
    i += 1
"""


for i in [0, 1, 2, "Hello"]:
    print(i)


# Instead of using a list we can actually use a range() function which allows us to specify the number of iterations, for example:
for _ in range(5): # We can use _ to assign a variable that iterates but then it is not used inside the condition
    print("meow")


print()

print("meow\n" * 3, end="")
