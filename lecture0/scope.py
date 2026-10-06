# SCOPE - A variable only exist in the context where it's defined

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to):
    print(f"Hi, {to} welcome back!")

main()


"""
This is the bad way, if we want to understand the concept of scope


def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("Hello,", name)

main()

"""