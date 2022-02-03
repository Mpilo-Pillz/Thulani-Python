from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multily(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "/": divide,
    "-": subtract,
    "+": add,
    "*": multily
}

def calculate():
   print(logo)
   continue_calculating = True
   first_number = float(input("What is the first number?: "))

   for operator in operators:
       print(operator)

   while continue_calculating:
       next_number = float(input("What is the next number"))
       operation = input("pick and operator from the list above")

       answer = operators[operation](first_number, next_number)
       print(f"{first_number} {operation} {next_number} = {answer}")

       should_continue = input(f"Press y to continue with the answer {answer} or n")

       if should_continue.lower() == "y":
          first_number = answer
       else:
           continue_calculating = False
           calculate()


calculate()