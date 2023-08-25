import sys

sys.stdin = open("1860_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # N : 사람수
    # M : 걸리는 시간
    # K : 만드는 개수
    N, M, K = map(int, input().split())
    ap = list(map(int, input().split()))  # 도착하는 사람 시간
    ap.sort()  # 도착시간 순으로 정렬

    result = "Possible"
    for i in range(N):
        if i + 1 > ap[i] // M * K:
            result = "Impossible"
            break

    print(f"#{tc} {result}")