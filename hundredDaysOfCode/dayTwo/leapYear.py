# leap year
# if year is divisible by 4 but not 100 unless it is divisible by 400
year_to_check = int(input("Enter the year\n"))

if year_to_check % 4 == 0:
    if year_to_check % 100 == 0 or year_to_check % 400 != 0:
        print(f"{year_to_check} is a leap year")
else:
    print("Not a leap year")