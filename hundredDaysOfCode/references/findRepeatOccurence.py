ints = [1, 3, 7, 5, 4, 3]
item = 3

indexes = [i for i in range(len(ints)) if ints[i] == item]
print(f"Item {item} is found at index {indexes}")