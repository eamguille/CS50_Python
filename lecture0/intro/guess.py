# Let's practice with a guess game

def get_guess():
    guess = int(input("Enter the number: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")


main()