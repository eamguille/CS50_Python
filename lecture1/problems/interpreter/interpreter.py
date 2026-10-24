
def main():
    expression = input("Expression: ")
    expression = expression.strip()

    print(calculate(expression))


def calculate(expression):
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    result = 0

    if not("+" in expression or "-" in expression or "*" in expression or "/" in expression):
        return "Error: Enter a valid operator"
    else:
        if y == "+": result = x + z
        elif y == "-": result = x - z
        elif y == "*": result = x * z
        else: result = x / z

    return f"{result:.1f}"


main()