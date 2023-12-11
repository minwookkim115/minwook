def cut(start, end):
    if end == 1:
        return
    for i in range(start + end // 3, start + (end // 3) * 2):
        cantor[i] = ' '
    cut(start, end // 3)
    cut(start + (end // 3) * 2, end // 3)


while True:
    try:
        n = int(input())
        cantor = ['-'] * 3 ** n
        cut(0, 3 ** n)
        print(''.join(cantor))
    except:
        break