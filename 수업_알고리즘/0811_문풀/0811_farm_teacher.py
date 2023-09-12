import sys
sys.stdin = open("농작물 수확_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    # 수확한 농작물
    crops = 0

    # 밭의 정중앙과의 거리가 d 이하인 곳만 수확
    d = N // 2

    # 밭 중앙 좌표
    center = (d, d)

    for r in range(N):
        for c in range(N):
            # 거리 계산 방법
            # abs|r - d| + abs|c - d| <= 3이면 농작물 수확
            if abs(r - d) + abs(c - d) <= d:
                crops += farm[r][c]

    print(f"#{tc} {crops}")