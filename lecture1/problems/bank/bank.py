
greeting = input("Greeting: ")

greeting = greeting.strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h") and "hello" not in greeting:
    print("$20")
else:
    print("$100")