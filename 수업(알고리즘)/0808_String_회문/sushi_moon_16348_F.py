import sys

sys.stdin = open("16348_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    al_list = [list(map(str, input())) for _ in range(N)]

    real_new_al_list = []

    for i in al_list:
        new_al_list = []
        for j in range(len(i)):
            new_al_list.append(i[N - 1 - j])

        real_new_al_list.append(new_al_list)

    al_list1 = []
    real_new_al_list1 = []

    for i in al_list:
        word = "".join(i)
        al_list1.append(word)

    for i in real_new_al_list:
        word = "".join(i)
        real_new_al_list1.append(word)

    for i in al_list1:
        for j in real_new_al_list1:
            if i == j:
                print(f"#{tc} {i}")