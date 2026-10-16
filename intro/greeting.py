
def greet(input):
    if "hello" in input:
        return "hello there"
    else:
        return "I'm not sure what you mean"


greeting = greet("hello, computer")

def get_name():
    username = input("Enter your name: ")
    return f"hmm, {greeting} {username}"


print(get_name())