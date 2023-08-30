import sys
sys.stdin = open("16905_input.txt", "r")

def winner(i, a, b):
    a.sort()
    if i == 3:
        return
    else:
        for j in range(3):


T = int(input())
for tc in range(1, T + 1):
    card_l = list(map(int, input().split()))

    p1 = []
    p2 = []

    check_p1 = []
    check_p2 = []

    answer = 0

    for i in range(12):
        if i % 2 == 0:
            p1.append(card_l[i])
        else:
            p2.append(card_l[i])

        if len(p1) >= 3:
            winner(0, p1, p2)
