logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
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
