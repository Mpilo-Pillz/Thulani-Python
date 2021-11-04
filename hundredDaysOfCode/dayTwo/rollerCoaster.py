print("Welcome to the roller coaster")
height = int(input("What is your height in cm? \n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?\n"))
    if age < 12:
        bill = 50
        print("Children pay R50.")
    elif age <= 20:
        bill = 70
        print("Teenagers pay R70.")
    else:
        bill = 120

    print("Adults pay R120")

    wants_photo = input("Do you want a photo taken? Typ Y or N\n")

    if (wants_photo == "Y"):
        bill += + 3
        print(f"Your final bill is {bill}")
else:
    print("Sorry but you are not tall enough to ride.")