T = int(input())

for tc in range(1, T + 1):
    n = int(input())  # 색칠 횟수

    paper = [[0] * 10 for _ in range(10)]  # 하양종이 10 * 10

    purple_count = 0  # 보라색 칸 개수 (겹친 개수)

    # n번 반복 하면서 색칠 하는데 겹친 칸 개수
    for i in range(n):
        sr, sc, er, ec, color = map(int, input().split())

        # 색칠 범위
        # 색칠 시작 행 ~ 색칠 끝 행
        for r in range(sr, er + 1):
            # 색칠 시작 열 ~ 색칠 끝 열
            for c in range(sc, ec + 1):
                # 색칠 하기 전에 봐야 할 것
                # 다른 색이 있다면 보라색이 된다.
                if paper[r][c] == 0:
                    paper[r][c] = color
                else:
                    # 0이 아니면 다른색이 칠해져 있었다.
                    purple_count += 1

    print(f"#{tc} {purple_count}")
