def calculate(first_num, second_num, operator):
    total = 0
    if (operator == "-"):
        total -= subtract(int(first_num), int(second_num))
    return total

def add(first_num, second_num):
    return f"{first_num} + {second_num} = {first_num + second_num}"

def subtract(first_num, second_num):
    return f"{first_num} - {second_num} = {first_num - second_num}"

def divide(first_num, second_num):
    if first_num == 0 or second_num == 0:
        return "error cannot divide by 0"
    return f"{first_num} / {second_num} = {first_num / second_num}"

def multiply(first_num, second_num):
    return f"{first_num} * {second_num} = {first_num * second_num}"