T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 0이 있는 하얀 10 * 10 종이
    paper = [[0] * 10 for _ in range(10)]

    # red 와 blue 겹치는 count
    purple_count = 0

    # N 번만큼 반복 / N == (칠할 좌표, 색깔) 개수
    for _ in range(N):

        # r1, c1 / r2, c2 => 색 칠할 좌표
        # color => red or blue
        # N번 반복해서 받기 때문에 for _ in range(N)을 통해 반복해서 받음
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2 + 1):  # 행 범위
            for c in range(c1, c2 + 1):  # 열 범위
                if paper[r][c] == 0:  # 0 이면
                    paper[r][c] = color  # 칠하고
                else:  # 0이 아니면 / 칠해져 있으면
                    purple_count += 1  # 겹치는 purple_count += 1

    print(f"#{tc} {purple_count}")
