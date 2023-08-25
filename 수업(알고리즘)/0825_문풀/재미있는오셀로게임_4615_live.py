import sys

sys.stdin = open("4615_input.txt", "r")


def f(i, j, bw, N):
    board[i][j] = bw  # 주어진 돌 놓기
    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i + di, j + dj

        temp = []
        #               보드 내부                      반대색이면
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            temp.append((ni, nj))
            ni, nj = ni + di, nj + dj
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:  # 보드 내부에 같은색이면
            for p, q in temp:
                board[p][q] = bw


B = 1
W = 2
op = [0, 2, 1]

T = int(input())
for tc in range(1, T + 1):
    # N : 보드크기
    # M : 돌 놓는 횟수
    N, M = map(int, input().split())
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]  # 0 -> N-1까지 인덱스 사용
    # 중심부에 4개 돌 배치
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W

    for col, row, bw in play:  # 입력이 col, row, color, / col,row는 인덱스 1 기준
        f(row - 1, col - 1, bw, N)  # 돌다 놓음
    # 흑돌, 백돌 개수 출력
    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1

    print(f"#{tc} {bcnt} {wcnt}")
