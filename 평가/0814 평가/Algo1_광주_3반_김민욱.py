import sys
sys.stdin = open("algo1_sample_in.txt", "r")

#    상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 가로 세로 크기
    mountain = [list(map(int, input().split())) for _ in range(N)]  # 확인할 지역

    bong = 0  # 봉우리의 개수
    for r in range(N):  # 행 순회
        for c in range(N):  # 열 순회
            count = 0  # 인접한 4곳이 모두 낮은지 count
            i = 0  # 인접한 곳을 몇군데 확인 했는지 count
            for k in range(4):  # 상하좌우 돌면서
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:  # 범위 안에 있으면
                    i += 1  # 확인한 곳 개수 + 1
                    if mountain[nr][nc] < mountain[r][c]:  # 상하좌우가 중앙보다 작으면
                        count += 1  # count에 + 1

            if count == i:  # 확인한 곳이 모두 낮으면
                bong += 1  # bong에 + 1

    print(f"#{tc} {bong}")
