def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multily(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multily,
    "/": divide
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for symbol in operations:
    print(symbol)


# opertion_symbol = int("Pick an ope")