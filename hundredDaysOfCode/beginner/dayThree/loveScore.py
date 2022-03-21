name_one = input("Whats is the name of the first person?")
name_two = input("What is the name of the second person")
combined_names = name_two + name_one
score = 0


loveScore = combined_names.lower().count("l") + combined_names.lower().count("o") + combined_names.lower().count("v") + combined_names.lower().count("e")
trueScore = combined_names.lower().count("t") + combined_names.lower().count("r") + combined_names.lower().count("u") + combined_names.lower().count("e")
score = int(str(loveScore) + str(trueScore))

print("love " + str(loveScore))
print("true " + str(trueScore))

if score < 10 or score > 90:
    print(f"{name_two} and {name_one} got together like coke and mentos")

if score >= 40 and score <= 50:
    print(f"Your score is {score} you would work out togther")

else:
    print(f"Score is {score}")