name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # Multiple cases in one line
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # Default case
        print("Who?")