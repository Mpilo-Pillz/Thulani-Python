# Write your code below this line 👇
def prime_checker(number):
    if number == 0:
        print("Zero is not prime")

    elif number > 0 and number < 4:
        print(f"{number} is prime")
    else:
        for num in range(number):
            print(num)

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)