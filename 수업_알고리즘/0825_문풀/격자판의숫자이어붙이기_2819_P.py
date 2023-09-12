import sys

sys.stdin = open("2819_input.txt", "r")

#    동  서  남  북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# dfs 함수
def dfs(string, r, c):
    # 문자열이 7개 되면
    if len(string) == 7:
        # check하기위해 append
        check.append(string)
        return
    # 동서남북
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            # 재귀로 돌기
            dfs(string + str(board[nr][nc]), nr, nc)


T = int(input())
for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]

    check = []
    for r in range(4):
        for c in range(4):
            # r c 돌면서 함수 돌기
            dfs(str(board[r][c]), r, c)

    # 세트로 없애고
    s_check = set(check)

    # 몇개인지 세기
    count = 0
    for i in s_check:
        count += 1

    print(f"#{tc} {count}")