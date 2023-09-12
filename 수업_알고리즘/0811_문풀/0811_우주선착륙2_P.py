import sys
sys.stdin = open("우주선_input2.txt", "r")

T = int(input())

# 위쪽부터 시계 방향 확인
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for r in range(N):
        for c in range(M):

            area_count = 0
            area = arr[r][c]
            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] < area:
                        area_count += 1

            if area_count >= 4:
                count += 1

    print(f"#{tc} {count}")