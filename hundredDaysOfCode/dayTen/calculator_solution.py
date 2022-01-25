from calculator_art import logo

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
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        num2 = float(input("What is the next number?: "))

        operation_symbol = input("Pick an operation: ")

        calculation_function = operations[operation_symbol]
        """
        operation_symbol["*"]
        {
        "*": multiply
        }
        multiply(num1, num2)
        """
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation:") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()