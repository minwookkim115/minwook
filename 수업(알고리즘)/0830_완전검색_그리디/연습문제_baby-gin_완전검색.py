"""
124783
667767
054060
101123
"""


def baby_gin(i, n):
    global answer
    if i == 6:
        if s_card[0] == s_card[1] == s_card[2]:
            if s_card[3] == s_card[4] == s_card[5]:
                print(s_card, "baby-gin")
            if s_card[3] + 1 == s_card[4] and s_card[4] + 1 == s_card[5]:
                print(s_card, "baby-gin")
        elif s_card[0] + 1 == s_card[1] and s_card[1] + 1 == s_card[2]:
            if s_card[3] == s_card[4] == s_card[5]:
                print(s_card, "baby-gin")
            if s_card[3] + 1 == s_card[4] and s_card[4] + 1 == s_card[5]:
                print(s_card, "baby_gin")
        else:
            print(s_card, "No")
        return
    else:
        for j in range(N):
            if used[j] == 0:
                s_card[i] = card[j]
                used[j] = 1
                baby_gin(i+1, n)
                used[j] = 0


card = list(map(int, input()))
N = len(card)
used = [0] * N
s_card = [0] * N

baby_gin(0, N)

answer = ""

# print(answer)
