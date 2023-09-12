import sys
sys.stdin = open("1234_input.txt", "r")

T = 10

for tc in range(1, T + 1):
    N, string = map(str, input().split())

    str_list = list(string)

    for _ in range(len(str_list) // 2):

        for i in range(len(str_list) - 1):
            if str_list[i] == str_list[i + 1]:
                str_list.pop(i + 1)
                str_list.pop(i)
                break

    num = "".join(str_list)
    print(f"#{tc} {num}")

