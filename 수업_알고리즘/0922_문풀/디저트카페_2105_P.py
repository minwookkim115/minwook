import sys

sys.stdin = open("2105_input.txt", "r")

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


# r, c 시작 좌표
# a = 사각형을 만들기 위한 기준
# check = 이미 한번 들린 숫자는 못들리기 때문에 check 배열
def find(r, c, a, check):
    # 전역변수 count
    global count

    # i+1, j-1 좌표가 사각형이 만들어졌을 때 좌표
    # 사각형이 만들어 졌으면
    if r == i + 1 and c == j - 1:
        # check에 들린곳이 모두 모여 있음
        # count에 들린곳 만큼 넣고 리턴
        if count <= len(check):
            count = len(check)
            return

    # 대각선 탐색 하면서
    for k in range(4):
        # 오른쪽아래, 왼쪽아래, 왼쪽위로 돌기 위해서
        # a(재귀들어온 k)를 기준으로 더 클때만 돌기
        if k >= a:
            nr = r + dr[k]
            nc = c + dc[k]
            # 범위안이고 check에 없으면
            if 0 <= nr < N and 0 <= nc < N and tour[nr][nc] not in check:
                # 재귀 들어가기
                find(nr, nc, k, check + [tour[nr][nc]])


T = int(input())
for tc in range(1, T + 1):

    N = int(input())  # 배열 길이
    tour = [list(map(int, input().split())) for _ in range(N)]  # 디저트 숫자
    count = 0  # 몇개의 디저트를 먹을 수 있을지

    # 대각선 사각형을 돌아야 할때
    # 시작점의 행이 0, N-2 사이
    # 시작점의 열이 1, N-1 사이에서만 사각형만들기 가능
    for i in range(N - 2):
        for j in range(1, N - 1):
            # 사각형 만들수 있는 좌표 돌면서 함수 돌리기
            find(i, j, -1, [tour[i][j]])

    # count가 4개 이상이 안되면 사각형이 안만들어 진것
    if count < 4:
        print(f"#{tc} {-1}")
    else:
        print(f"#{tc} {count}")
