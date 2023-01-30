def chunk(array, size):
    chunked = []
    for item in array:
        last_item = []
        if len(chunked) >= 1:
            last_item = chunked[len(chunked) - 1]

        if not last_item or len(last_item) == size:
            chunked.append([item])
        else:
            last_item.append(item)

    return chunked


print(chunk([1, 2, 3, 4], 2))
print(chunk([1, 2, 3, 4, 5], 2))
print(chunk([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(chunk([1, 2, 3, 4, 5], 4))
print(chunk([1, 2, 3, 4, 5], 10))
