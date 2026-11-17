
# Lists and dictionaries comprehensions are shorter forms and more directly to create a new list or new dictionary based on other iterable, but just in one line of code.

def main():
    words = ["Hello", "my", "name", "is", "Guillermo", "Castillo", "name"]
    lowercase_words = [word.lower() for word in words if len(word) > 3]
    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    print(counts)


main()