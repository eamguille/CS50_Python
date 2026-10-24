
question = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

question = question.strip().lower()

if not (question == "42" or question == "forty-two" or question == "forty two"):
    print("No")
else:
    print("Yes")