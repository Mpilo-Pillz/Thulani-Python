def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(n1, n2, operatorFunction):
    return operatorFunction(n1, n2)
    # return operatorFunction(n1, n2)


print(calculate(3,4, add))
print(calculate(3,4, subtract))
print(calculate(3,4, multiply))
print(calculate(3,4, divide))