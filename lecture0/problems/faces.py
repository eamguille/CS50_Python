
def convert(txt):
    return txt.replace(":)", "🙂").replace(":(", "🙁")

def main():
    text = input()
    print(convert(text))

main()