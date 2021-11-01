# #comment
# print("Day 1 - String Manipulation")
# print("String concatenation is done with the '+' sign.")
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")
# #
# # name = input("What is yout name")
# # print("What is your name? " + name)
# # print(str(len(name)))
#
# ###
# print(len(input("What is your name")))

#######
cupOne = "Juice"
cupTwo = "Tea"

emptyCup = "empty"

print("In cup one we have " + cupOne)
print("In cup two we have " + cupTwo + "\n")

print("then we pur out he cups\n")

#pour cup one into empty cup an dmake cup one empty
emptyCup = cupOne
cupOne = "empty"

print("In cup one we have " + cupOne)
print("In empty cup we have " + emptyCup)

print("\nNow we move cupTwo\n")


cupOne = cupTwo
cupTwo = " empty"
print("In cup one we now have " + cupOne)
print("empty cup has " + emptyCup)
print("cupTwo now has " + cupTwo)

print("\nempty emty cum\n")
cupTwo = emptyCup
emptyCup = "empty"

print("cup one has " + cupOne)
print("cup two now has " + cupTwo)
print("empty cup now has " + emptyCup)




