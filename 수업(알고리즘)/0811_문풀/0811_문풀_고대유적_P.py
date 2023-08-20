import sys

sys.stdin = open("고대유적_input1.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0

    for r in range(N):
        for c in range(M):
            r_count = 0
            if arr[r][c] == 1:
                r_count += 1
                for nc in range(c + 1, M):
                    if arr[r][nc] == 1:
                        r_count += 1
                        continue
                    else:
                        break
            if max_len < r_count:
                max_len = r_count

    for c in range(M):
        for r in range(N):
            c_count = 0
            if arr[r][c] == 1:
                c_count += 1
                for nr in range(r + 1, N):
                    if arr[nr][c] == 1:
                        c_count += 1
                        continue
                    else:
                        break
            if max_len < c_count:
                max_len = c_count

    print(f"#{tc} {max_len}")
