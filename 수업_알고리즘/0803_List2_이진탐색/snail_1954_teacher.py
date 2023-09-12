T = int(input())

# d = 0 오른쪽
# d = 1 아래
# d = 2 왼쪽
# d = 3 위쪽
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T + 1):
    N = int(input())

    # 달팽이 집을 0 으로 다 채워서 N * N 만큼 만들어 주기

    snail = [[0] * N for _ in range(N)]

    # 달팽이집 채우기 시작좌표 (0,0)
    # N * N 번 반복하면서 채워 간다.
    # 방향은 우 => 하 => 좌 => 상 => 우 ......

    # d 는 채워 나가는 방향
    d = 0
    # 시작위치
    r, c = 0, 0
    for i in range(1, (N * N) + 1):
        snail[r][c] = i  # 이게 먼소리고

        # 다음 방향으로 진행
        # 다음 위치가 유효한 위치인지
        nr = r + dr[d]
        nc = c + dc[d]

        # 다음 위치가 유효하지 않으면 방향 꺾기
        # nr, nc 가 인덱스 범위 안에있어야 하고
        # 다음 위치가 0이 아니면 방향 꺾기
        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
            # 다음 위치가 유효하면 계속 가고
            r, c = nr, nc
        else:
            # 유효하지 않으면 방향 꺾기
            # d = d + 1 if d < 3 else 0
            # if d < 3:
            #     d + 1
            # else:
            #     0
            d = (d + 1) % 4
            r = r + dr[d]
            c = c + dc[d]
    print(f"#{tc}")
    for i in range(N):
        print(" ".join(map(str, snail[i])))
