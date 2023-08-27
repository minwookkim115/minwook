import sys
sys.stdin = open("1289_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    memory = list(input())

    count = 0
    check = "0"
    for i in range(len(memory)):
        if check == "0":
            if memory[i] != check:
                count += 1
                check = "1"
        else:
            if memory[i] != check:
                count += 1
                check = "0"

    print(f"#{tc} {count}")