
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    # return True if n % 2 == 0 else False # This version is more compact
    return n % 2 == 0 # This one is even more compact

main()


"""
We can actually convert these 4 lines of code

    if n % 2 == 0:
        return True
    else:
        return False


Into this

    return True if n % 2 == 0 else False


And even more compact

    return (n % 2 == 0)
"""