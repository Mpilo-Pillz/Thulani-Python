for num in range(1, 101):
    divisible_by_three = num % 3 == 0
    divisible_by_five = num % 5 == 0

    if divisible_by_three and divisible_by_five:
        print("Fizz Buzz")
    elif divisible_by_three:
        print("Fizz")
    elif divisible_by_five:
        print("Buzz")
    else:
        print(num)
        