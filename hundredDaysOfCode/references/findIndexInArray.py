string='mississippi'
s='s'
lst= []
for i in range(len(string)):
    if (string[i] == s):
        lst.append(i)
print(lst)
#result: [2, 3, 5, 6]
