import sys

sys.stdin = open("in.txt", "r")

T = int(input())


def is_vaild(r, c):
    return 0 <= r < N and 0 <= c < N


for tc in range(1, T + 1):
    N = int(input())

    # 상하좌우(델타)
    # (행의 좌표, 열의 좌표)
    # (r, c)
    # dr 은 행 번호의 변화량
    # dc 는 열 번호의 변화량
    # 0=상, 1=하, 2=좌, 3=우
    # 상(-1,0) 하(1,0) 좌(0,-1) 우(0,1) 만큼 변한다
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 2차원 배열 입력 받기
    # list(......) => 한줄 입력받기(1차원 배열)
    # for _ in range(N) => N 번 입력 받아 2차원 배열로 만듬
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 배열 탐색
    # 행우선으로

    diff_sum = 0
    for r in range(N):  # 가로와 세로의 길이가 같으니까 행도 N 열도 N
        for c in range(N):
            # 현재위치 가 r행 c열 (r, c)
            # matrix[r][c] => 현재 위치에 저장된 원소
            # print(f"현재 위치 : ({r},{c}), 값 : {matrix[r][c]}")

            # 현재위치에서 상하좌우 차이 절대값의 합
            now_diff_sum = 0

            # 상하좌우 탐색
            # d = 0(상), 1(하), 2(좌), 3(우)
            for d in range(4):
                # d 는 델타배열의 인덱스
                # 현재위치는 (r,c) 상하좌우로 이동후 위치(nr, nc)
                nr = r + dr[d]  # 다음 행 번호 = 현재 행 번호 + 이동방향이 d일때 변화량
                nc = c + dc[d]  # 다음 열 번호 = 현재 열 번호 + 이동방향이 d일때 변화량

                # 내가 계산한 위치가 유효한 인덱스 인지(배열의 범위 안에 있는지) 검사
                # if is_vaild(nr, nc):
                if 0 <= nr < N and 0 <= nc < N:
                    # 차이 = 현재위치값 - 움직인 위치에 있는 값
                    diff = matrix[r][c] - matrix[nr][nc]
                    diff = -diff if diff < 0 else diff

                    now_diff_sum += diff

            # 상하좌우 탐색이 끝나면 현재 위치 절대값 차이의 합이 구해졌다.
            diff_sum += now_diff_sum

    print(f"#{tc} {diff_sum}")

