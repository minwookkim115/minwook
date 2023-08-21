import sys
sys.stdin = open("16692_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    ch_l = [0] * (N + 1)
    ch_r = [0] * (N + 1)

    num = 0

    def inorder(t):
        inorder(ch_l[t])
        t += 1



    inorder(num)