from calculator_art import logo

print(logo)
first_number = int(input("What is the first number?: "))
def calculate():
    second_number = int(input("What is the next number?: "))
    print(operators)
    operation = input("Chose from the list of operators above to perform a calculation: ")
    # answer = performCalculation(operators[operation], first_number, second_number)
    answer = operators[operation](first_number, second_number) # too fancy
    return f"{first_number} {operation} {second_number} = {answer}"


def add(first_num, second_num):
    return first_num + second_num
    # return f"{first_num} + {second_num} = {first_num + second_num}"

def subtract(first_num, second_num):
    return first_num - second_num
    # return f"{first_num} - {second_num} = {first_num - second_num}"

def divide(first_num, second_num):
    if first_num == 0 or second_num == 0:
        return "error cannot divide by 0"
    return first_num / second_num
    # return f"{first_num} / {second_num} = {first_num / second_num}"

def multiply(first_num, second_num):
    return first_num * second_num
    # return f"{first_num} * {second_num} = {first_num * second_num}"

def performCalculation(operation, num1, num2):
    return operation(num1, num2)

operators = {
    '*': multiply,
    '/': divide,
    '+': add,
    '-': subtract
}

print(calculate())

