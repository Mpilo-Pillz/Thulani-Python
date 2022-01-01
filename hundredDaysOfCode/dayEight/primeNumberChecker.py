# Write your code below this line 👇
def prime_checker(number):
    is_prime = False
    if number == 0:
        print("Zero is not prime")

    elif number > 0 and number < 4:
        is_prime = True
    else:
        for num in range(2, number):
            # print(num)
            if number % num == 0:
                is_prime = False
                break
            else:
                is_prime = True

    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is NOT prime")
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)