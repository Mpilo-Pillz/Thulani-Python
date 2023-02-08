def recursiveReduce(num):

    if num > 0:
        num = num + recursiveReduce(num - 1)
    return num

print(recursiveReduce(5))

