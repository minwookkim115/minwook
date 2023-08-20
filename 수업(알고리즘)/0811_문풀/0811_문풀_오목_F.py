import sys
sys.stdin = open("오목_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    answer = "NO"

    for r in range(N):
        for c in range(N):
            o_count_r = 0
            if arr[r][c] == "o":
                o_count_r += 1
                for nc in range(c + 1, N):
                    if arr[r][nc] == "o":
                        o_count_r += 1
                        continue
                    else:
                        break
            if o_count_r >= 5:
                answer = "YES"

    for c in range(N):
        for r in range(N):
            o_count_c = 0
            if arr[r][c] == "o":
                o_count_c += 1
                for nr in range(r + 1, N):
                    if arr[nr][c] == "o":
                        o_count_c += 1
                        continue
                    else:
                        break
            if o_count_c >= 5:
                answer = "YES"

    for r in range(N):
        o_count_x = 0
        if arr[r][r] == "o":
            for nr in range(r + 1, N):
                if arr[nr][nr] == "o":
                    o_count_x += 1
                    continue
                else:
                    break
        if o_count_x >= 5:
            answer = "YES"

    for r in range(N):
        for c in range(N-1, -1, -1):
            o_count_y = 0
            if arr[r][c] == "o":
                for nr in range(r - 1, -1, -1):
                    for nc in range(N-2, -1, -1):
                        if arr[nr][nc] == "o":
                            o_count_y += 1
                        continue
                    else:
                        break
            if o_count_y >= 5:
                answer = "YES"

    print(f"#{tc} {answer}")