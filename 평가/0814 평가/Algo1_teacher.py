import sys

sys.stdin = open("algo1_sample_in.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 지형 정보
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 봉우리의 수
    count = 0

    # 모든 (r, c)를 검사해서 r,c가 봉우리가 되는지 확인
    for r in range(N):
        for c in range(N):

            # (r,c)에서 상하좌우 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                # nr, nc가 유요한 인덱스 범위인지 확인
                if 0 <= nr < N and 0 <= nc < N:
                    # (nr, nc)가 (r, c)보다 높아버리면 안된다.
                    if arr[r][c] <= arr[nr][nc]:
                        break
            else:
                # 중간에 (r,c)이상인 (nc,nc)가 없었다면 실행
                count += 1
    print(f"#{tc} {count}")
