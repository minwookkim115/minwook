for i in range(5):
    for j in range(5):
        if i == j:
            j = '#'
        else :
            j = '+'
        print(j, end='')
    print()