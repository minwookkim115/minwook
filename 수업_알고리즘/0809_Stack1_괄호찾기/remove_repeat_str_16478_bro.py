import sys

sys.stdin = open("16478_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    s = input()

    lst = list(s)

    for _ in range(len(s) // 2):

        for i in range(0, len(lst) - 1):
            if lst[i] == lst[i + 1]:
                lst.pop(i + 1)
                lst.pop(i)
                break

    print(f"#{tc} {len(lst)}")
