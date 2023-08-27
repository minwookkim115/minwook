import sys

sys.stdin = open("1873_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())  # 맵의 높이와 넓이
    field = [list(input()) for _ in range(H)]  # 맵
    N = int(input())  # 명령 개수
    move = list(input())  # 움직일 명령

    r = 0  # 시작 행 번호
    c = 0  # 시작 열 번호

    # ^v<> 있는 곳이 시작
    for r1 in range(H):
        for c1 in range(W):
            if field[r1][c1] in "^v<>":
                r = r1
                c = c1

    # 움직일 명령 돌면서
    for i in move:
        if i == "S":  # 슛 일때
            if field[r][c] == "^":  # 위보고 있으면
                for j in range(r, -1, -1):  # 위쪽으로
                    if field[j][c] == "#":  # 강철이면
                        break  # 끝내고
                    if field[j][c] == "*":  # 벽돌이면
                        field[j][c] = "."  # 뿌수고
                        break # 끝내고
            # 아래보고 있으면
            # 반복
            elif field[r][c] == "v":
                for j in range(r, H):
                    if field[j][c] == "#":
                        break
                    if field[j][c] == "*":
                        field[j][c] = "."
                        break
            elif field[r][c] == "<":
                for j in range(c, -1, -1):
                    if field[r][j] == "#":
                        break
                    if field[r][j] == "*":
                        field[r][j] = "."
                        break
            elif field[r][c] == ">":
                for j in range(c, W):
                    if field[r][j] == "#":
                        break
                    if field[r][j] == "*":
                        field[r][j] = "."
                        break
        # U일때
        if i == "U":
            field[r][c] = "^"  # 위로 바꾸고
            if 0 <= r - 1 < H and field[r - 1][c] == ".":  # 범위안에 있고, 평지면
                field[r - 1][c] = "^"  # 움직이고
                field[r][c] = "."  # 있던자리 평지로 만들고
                r = r - 1  # 전차 좌표 옮기기
        # D일때
        # 계속 반복
        if i == "D":
            field[r][c] = "v"
            if 0 <= r + 1 < H and field[r + 1][c] == ".":
                field[r + 1][c] = "v"
                field[r][c] = "."
                r = r + 1
        if i == "L":
            field[r][c] = "<"
            if 0 <= c - 1 < W and field[r][c - 1] == ".":
                field[r][c - 1] = "<"
                field[r][c] = "."
                c = c - 1
        if i == "R":
            field[r][c] = ">"
            if 0 <= c + 1 < W and field[r][c + 1] == ".":
                field[r][c + 1] = ">"
                field[r][c] = "."
                c = c + 1

    # 리스트 묶어서 리스트에 넣고
    field_l = []
    for i in field:
        a = "".join(i)
        field_l.append(a)

    # tc 출력
    print(f"#{tc}", end=' ')
    for i in field_l:
        # 묶은거 출력
        print(i)
