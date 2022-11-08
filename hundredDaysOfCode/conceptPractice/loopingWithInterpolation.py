dev_weapons = ["Keychron K4 blue", "Apple Magic Keyboard", "Keychron K2 brown", "Lenovo MX Master 3", "Apple Magic mouse"]

for index, dev_weapon in enumerate(dev_weapons):
    print(f"{dev_weapon} - {index}")

print("________________________________")
for i in range(len(dev_weapons)):
    if i == len(dev_weapons) - 1:
        print(f"{dev_weapons[i]}")
    else:
        print(f"{dev_weapons[i]},")

print("---------------------------")
dev_weapons_in_a_string = ""
for i in range(len(dev_weapons)):
    if i == len(dev_weapons) - 1:
        dev_weapons_in_a_string += f"{dev_weapons[i]}"
        print(dev_weapons_in_a_string)
    else:
        dev_weapons_in_a_string += f"{dev_weapons[i]}, "
        print(dev_weapons_in_a_string)



