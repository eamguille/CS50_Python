
def main():
    w = int(input("What's w? "))
    h = int(input("What's h? "))

    print_shape(h, w)


def print_shape(h, w):
    for i in range(h):
        for j in range(w):
            print("#", end="")
        print()


main()