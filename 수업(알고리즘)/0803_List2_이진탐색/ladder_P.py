T = 10

N = 100

for tc in range(1, T + 1):
    int(input())

    ladder = [list(map(int, input().split())) for _ in range(N)]

    r = 99
    c = 0

    for i in range(N):
        if ladder[r][i] == 2:
            c = i

    # 좌우 먼저보고 없으면 위로 이동
    # 좌우 값 먼저
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    # 끝은 알지만 몇번 반복할지 모를 때 while 사용
    while r > 0:

        for d in range(3):

            nr = r + dr[d]  # 이동할 행 값
            nc = c + dc[d]  # 이동할 열 값

            if 0 <= nr < N and 0 <= nc < N and ladder[nr][nc] == 1:  # 갈곳이 1이면
                r = nr
                c = nc

                # if 안에서 움직이니까 안에서 실행
                ladder[r][c] = 0  # 이동한 칸은 0으로 바꿈

                break  # 왼쪽, 오른쪽, 위에 1이 있으면 이동하고 for 문 처음으로 다시 이동

    print(f"#{tc} {c}")
