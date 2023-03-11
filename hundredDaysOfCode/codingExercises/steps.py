'#  '
'## '
'###'
def step(n):
    for row in range(n):
        step = ""
        for column in range(n):
            if (column <= row):
                step += '#'
            else:
                step += ' '

        print(step)


step(5)