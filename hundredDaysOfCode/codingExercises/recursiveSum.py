def recursiveSum(num):
    if num > 0:
        return num + recursiveSum(num - 1)
    return num


print(recursiveSum(5))