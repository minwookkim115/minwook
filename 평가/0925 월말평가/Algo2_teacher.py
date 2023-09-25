import sys

sys.stdin = open("algo2_sample_in.txt", "r")

T = int(input())


def shoot(r, selected, score):
    global max_score

    # 종료
    if r == N:
        max_score = max(max_score, score)
        return

    # 재귀
    for c in range(N):
        if not selected[c]:
            selected[c] = 1
            shoot(r + 1, selected, score + arr[r][c])
            selected[c] = 0


for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대점수
    max_score = 0

    shoot(0, [0] * N, 0)

    print(f"#{tc} {max_score}")
