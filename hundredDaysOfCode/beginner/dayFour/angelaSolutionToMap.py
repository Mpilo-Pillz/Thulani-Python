# π¨ Don't change the code below π
row1 = ["β¬οΈ","β¬οΈ","β¬οΈ"]
row2 = ["β¬οΈ","β¬οΈ","β¬οΈ"]
row3 = ["β¬οΈ","β¬οΈ","β¬οΈ"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# π¨ Don't change the code above π

#Write your code below this row π
horizontal = int(position[0])
vertical = int(position[1])

# selected_row = map[vertical - 1]
# print("-->",selected_row)
# # selected row is a row oor an entire array
# # cos we have selected it we now pic an index of of it
# selected_row[horizontal - 1] = "π"

map[vertical - 1][horizontal - 1] = "πΊπΎ"

#Write your code above this row π

# π¨ Don't change the code below π
print(f"{row1}\n{row2}\n{row3}")